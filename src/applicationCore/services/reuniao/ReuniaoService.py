
from datetime import datetime, date, timedelta
from typing import List, Tuple
from src.adapters.NotifierAdapter import NotifierAdapter
from src.applicationCore.domain.reuniao.Convidado import Convidado
from src.applicationCore.domain.reuniao.Lembrete import Lembrete
from src.applicationCore.domain.reuniao.Reuniao import Reuniao
from src.applicationCore.domain.reuniao.IReuniaoRepository import IReuniaoRepository
from src.applicationCore.domain.reuniao.SalaEncontro import SalaEncontro
from src.applicationCore.domain.usuario.IUsuarioRepository import IUsuarioRepository
from src.applicationCore.domain.usuario.Usuario import Usuario
from src.applicationCore.services.exceptions.ReuniaoException import ConvidadoNotFound, ReuniaoNotFound
from src.applicationCore.services.exceptions.UsuarioException import UsuarioNotFound
from src.applicationCore.services.reuniao.ReuniaoDTO import ReuniaoDTO
from src.applicationCore.services.usuario.UsuarioBasico import UsuarioBasico


class ReuniaoService():
    _reuniaoRepository: IReuniaoRepository
    _usuarioRepository: IUsuarioRepository
    _notificadores: List[NotifierAdapter]
    _usuarioLogado: UsuarioBasico

    def __init__(self, reuniaoRepo: IReuniaoRepository, usuarioRepo: IUsuarioRepository,
                 notificadores: List[NotifierAdapter], usuarioLogado: UsuarioBasico) -> None:
        self._reuniaoRepository = reuniaoRepo
        self._notificadores = notificadores
        self._usuarioRepository = usuarioRepo
        self._usuarioLogado = usuarioLogado

    def buscaReunioesDaSemanaPorUsuarioLogado(self) -> List[Reuniao]:

        dataInicio, dataTermino = self.__obterSemanaDeTrabalho()

        reunioes = self._reuniaoRepository.findAllBetweenDataInicioAndDataTerminoFromUsuario(
            dataInicio, dataTermino, self._usuarioLogado.id)

        return reunioes

    def buscaReuniaoPorId(self, reuniaoId: int) -> Reuniao:

        reuniao = self._reuniaoRepository.findById(reuniaoId)

        if not reuniao:
            raise ReuniaoNotFound(reuniaoId)

        return reuniao

    def buscaReunioesPorPeriodo(self, dataInicio: date, dataFim: date, usuarioLogado: Usuario) -> List[Reuniao]:

        reunioes = self._reuniaoRepository.findAllBetweenDataInicioAndDataTerminoFromUsuario(
            dataInicio, dataFim, usuarioLogado.id)

        return reunioes

    def criarReuniao(self, reuniaoDto: ReuniaoDTO) -> int:

        host = self._usuarioRepository.findByUsername(
            self._usuarioLogado.username)

        convidadosEncontrados: List[Convidado] = list()

        for username in reuniaoDto.convidadosUsernames:
            usuario = self._usuarioRepository.findByUsername(username)

            if not usuario:
                raise ConvidadoNotFound(username)

            convidado = Convidado(True, usuario)
            convidadosEncontrados.append(convidado)

        novaReuniao = Reuniao(reuniaoId=0,
                              titulo=reuniaoDto.titulo,
                              pauta=reuniaoDto.pauta,
                              dataInicio=reuniaoDto.dataInicio,
                              dataTermino=reuniaoDto.dataFim,
                              host=host,
                              sala=reuniaoDto.local,
                              lembrete=reuniaoDto.lembrete,
                              convidados=reuniaoDto.convidadosEncontrados,
                              notificadores=self._notificadores)

        novaReuniaoId = self._reuniaoRepository.save(novaReuniao)
        novaReuniao.id = novaReuniaoId

        self.__notificarReuniao(novaReuniao)
        return novaReuniaoId

    def atualizarReuniao(self, reuniaoDto: ReuniaoDTO) -> bool:

        host = self._usuarioRepository.findByUsername(
            self._usuarioLogado.username)

        if not host:
            raise UsuarioNotFound(self._usuarioLogado.username)

        reuniao = self._reuniaoRepository.findById(
            reuniaoId=reuniaoDto.reuniaoId)

        if not reuniao or reuniao.host.id != host.id:
            raise ReuniaoNotFound(reuniaoDto.reuniaoId)

        convidadosAtuais = reuniao.convidados

        convidadosUsernamesAtuais = [
            c.usuario.username for c in convidadosAtuais]

        convidadosParaRemover = set(convidadosUsernamesAtuais).difference(
            set(reuniaoDto.convidadosUsernames))

        for cr in convidadosParaRemover:
            for convidado in convidadosAtuais:
                if convidado.usuario.username == cr:
                    reuniao.removerConvidado(convidado=convidado)

        novosConvidados = set(reuniaoDto.convidadosUsernames).difference(
            set(convidadosUsernamesAtuais))

        for username in novosConvidados:
            usuario = self._usuarioRepository.findByUsername(username)

            if not usuario:
                raise ConvidadoNotFound(username)

            convidado = Convidado(True, usuario)
            reuniao.adicionarConvidado(convidado=convidado)

        reuniao.titulo = reuniaoDto.titulo
        reuniao.pauta = reuniaoDto.pauta
        reuniao.status = reuniaoDto.status
        reuniao.lembrete = reuniaoDto.lembrete
        reuniao.dataInicio = reuniaoDto.dataInicio
        reuniao.dataTermino = reuniaoDto.dataFim
        reuniao.notificadores = self._notificadores

        self._reuniaoRepository.update(reuniao)

        self.__notificarReuniao(reuniao)

        return True

    def cancelarReuniao(self, reuniaoId: int) -> bool:

        host = self._usuarioRepository.findByUsername(
            self._usuarioLogado.username)

        if not host:
            raise UsuarioNotFound(self._usuarioLogado.username)

        reuniao = self._reuniaoRepository.findById(reuniaoId=reuniaoId)

        if not reuniao or reuniao.host.id != host.id:
            raise ReuniaoNotFound(reuniaoId)

        reuniao.cancelarReuniao()

        self._reuniaoRepository.update(reuniao=reuniao)

        return True

    def __notificarReuniao(self, reuniao: Reuniao) -> bool:

        for notificador in self._notificadores:
            for convidado in reuniao.convidados:
                notificador.enviarNotificacao(rementente=convidado)

        return True

    def __obterSemanaDeTrabalho() -> Tuple:

        dataInicio = dataTermino = date.today()
        diaDaSemana = dataInicio.weekday()
        """
            se dia da semana for sábado ou domingo, busca as reuniões da próxima semana
        """
        if diaDaSemana > 4:
            dataInicio = dataInicio + \
                timedelta(days=-diaDaSemana, weeks=1)

        elif diaDaSemana != 0:
            dataInicio = dataInicio - timedelta(days=diaDaSemana)

        dataTermino = dataInicio + timedelta(days=4)

        return dataInicio, dataTermino
