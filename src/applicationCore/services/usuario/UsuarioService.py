
from typing import List

from src.applicationCore.domain.usuario.IUsuarioRepository import \
    IUsuarioRepository
from src.applicationCore.services.exceptions.UsuarioException import \
    UsuarioErrorCredentials
from src.applicationCore.services.usuario.UsuarioBasico import UsuarioBasico
from src.applicationCore.services.usuario.UsuarioFactory import UsuarioFactory
from src.utils.password_utils import encrypt_password


class UsuarioService():
    _usuarioRepository: IUsuarioRepository
    _usuarioFactory: UsuarioFactory

    def __init__(self, usuarioRepo: IUsuarioRepository) -> None:
        self._usuarioRepository = usuarioRepo
        self._usuarioFactory = UsuarioFactory()

    def fazerLogin(self, user: str, senha: str) -> UsuarioBasico:
        senha_encriptada = encrypt_password(senha)
        usuario = self._usuarioRepository.findByUsernameAndSenha(
            username=user, senha_encriptada=senha_encriptada)

        if not usuario:
            raise UsuarioErrorCredentials()

        return self._usuarioFactory.obterUsuarioBasico(usuario)

    def buscaUsuariosPorNomeOuUsername(self, palavras: List[str]) -> List[UsuarioBasico]:
        encontrados = self._usuarioRepository.findByNomeOrUsername(palavras)
        usuarios: List[UsuarioBasico] = list()

        for u in encontrados:
            usuarios.append(self._usuarioFactory.obterUsuarioBasico(u))

        return usuarios
