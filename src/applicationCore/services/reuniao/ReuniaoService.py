
from datetime import datetime
from typing import List
from src.adapters.NotifierAdapter import NotifierAdapter
from src.applicationCore.domain.reuniao.Lembrete import Lembrete
from src.applicationCore.domain.reuniao.Reuniao import Reuniao
from src.applicationCore.domain.reuniao.IReuniaoRepository import IReuniaoRepository
from src.applicationCore.domain.reuniao.SalaEncontro import SalaEncontro
from src.applicationCore.domain.usuario.Usuario import Usuario
from src.applicationCore.services.usuario.UsuarioBasico import UsuarioBasico


class ReuniaoService():
    _reuniaoRepository: IReuniaoRepository
    _notificadores: List[NotifierAdapter]
    _usuarioLogado: UsuarioBasico

    def __init__(self, reuniaoRepo: IReuniaoRepository, usuarioLogado: UsuarioBasico, notificadores: List[NotifierAdapter]) -> None:
        self._reuniaoRepository = reuniaoRepo
        self._usuarioLogado = usuarioLogado
        self._notificadores = notificadores

    def buscaReunioesPorUsuarioLogado() -> List[Reuniao]:
        pass

    def buscaReuniaoPorId(reuniaoId: int) -> Reuniao:
        pass

    def buscaReunioesPorPeriodo(dataInicio: datetime, dataFim: datetime, usuarioLogado: UsuarioBasico) -> List[Reuniao]:
        pass

    def criarReuniao(titulo: str, pauta: str, dataInicio: datetime, dataFim: datetime,
                     local: SalaEncontro, lembrete: Lembrete, convidados: List[int]) -> int:
        pass

    def atualizarReuniao(reuniao: Reuniao) -> bool:
        pass

    def cancelarReuniao(reuniaoId: int) -> bool:
        pass

    def __notificarReuniao() -> bool:
        pass
