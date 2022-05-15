
from datetime import datetime, date, timedelta
from typing import List, Tuple
from src.adapters.NotifierAdapter import NotifierAdapter
from src.applicationCore.domain.reuniao.Lembrete import Lembrete
from src.applicationCore.domain.reuniao.Reuniao import Reuniao
from src.applicationCore.domain.reuniao.IReuniaoRepository import IReuniaoRepository
from src.applicationCore.domain.reuniao.SalaEncontro import SalaEncontro
from src.applicationCore.domain.usuario.Usuario import Usuario
from src.applicationCore.services.exceptions.ReuniaoException import ReuniaoNotFound
from src.applicationCore.services.usuario.UsuarioBasico import UsuarioBasico


class ReuniaoService():
    _reuniaoRepository: IReuniaoRepository
    _notificadores: List[NotifierAdapter]
    _usuarioLogado: Usuario

    def __init__(self, reuniaoRepo: IReuniaoRepository, usuarioLogado: Usuario, notificadores: List[NotifierAdapter]) -> None:
        self._reuniaoRepository = reuniaoRepo
        self._usuarioLogado = usuarioLogado
        self._notificadores = notificadores

    def buscaReunioesDaSemanaPorUsuarioLogado(self) -> List[Reuniao]:

        dataInicio, dataTermino = self.__obterSemanaDeTrabalho()

        reunioes = self._reuniaoRepository.findAllBetweenDataInicioAndDataTerminoFromUsuario(
            dataInicio, dataTermino, self._usuarioLogado.id)

        return reunioes

    def buscaReuniaoPorId(self, reuniaoId: int) -> Reuniao:

        reuniao = self._reuniaoRepository.findById(reuniaoId)

        if not reuniao:
            raise ReuniaoNotFound()

        return reuniao

    def buscaReunioesPorPeriodo(self, dataInicio: date, dataFim: date, usuarioLogado: Usuario) -> List[Reuniao]:

        reunioes = self._reuniaoRepository.findAllBetweenDataInicioAndDataTerminoFromUsuario(
            dataInicio, dataFim, usuarioLogado.id)

        return reunioes

    def criarReuniao(self, titulo: str, pauta: str, dataInicio: datetime, dataFim: datetime,
                     local: SalaEncontro, lembrete: Lembrete, convidados: List[int]) -> int:
        pass

    def atualizarReuniao(self, reuniao: Reuniao) -> bool:
        pass

    def cancelarReuniao(self, reuniaoId: int) -> bool:
        pass

    def __notificarReuniao(self) -> bool:
        pass

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
