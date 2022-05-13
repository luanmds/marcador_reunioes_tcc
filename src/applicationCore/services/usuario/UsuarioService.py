
from typing import List
from src.applicationCore.services.usuario.UsuarioBasico import UsuarioBasico
from src.applicationCore.services.usuario.UsuarioFactory import UsuarioFactory
from src.applicationCore.domain.usuario.IUsuarioRepository import IUsuarioRepository


class UsuarioService():
    _usuarioRepository: IUsuarioRepository
    _usuarioFactory: UsuarioFactory

    def __init__(self, usuarioRepo: IUsuarioRepository) -> None:
        self._usuarioRepository = usuarioRepo
        self._usuarioFactory = UsuarioFactory()

    def fazerLogin(user: str, senha: str) -> UsuarioBasico:
        pass

    def buscaUsuariosDisponiveis() -> List[UsuarioBasico]:
        pass
