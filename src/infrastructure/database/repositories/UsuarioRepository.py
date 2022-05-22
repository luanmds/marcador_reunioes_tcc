
from typing import List, Optional

from src.adapters.DatabaseConnectionAdapter import DatabaseConnectionAdapter
from src.applicationCore.domain.usuario.DadosPessoais import DadosPessoais
from src.applicationCore.domain.usuario.IUsuarioRepository import \
    IUsuarioRepository
from src.applicationCore.domain.usuario.Usuario import Usuario
from src.infrastructure.database.models.UsuarioModel import UsuarioModel


class UsuarioRepository(IUsuarioRepository):

    def __init__(self, dbConnection: DatabaseConnectionAdapter) -> None:
        super().__init__(dbConnection)

    def findById(self, usuarioId: int) -> Optional[Usuario]:
        raise NotImplementedError

    def findByNomeOrUsername(self, palavras: List[str]) -> List[Usuario]:
        raise NotImplementedError

    def findByUsername(self, username: str) -> Optional[Usuario]:
        raise NotImplementedError

    def findByUsernameAndSenha(self, username: str, senha_encriptada: str) -> Optional[Usuario]:

        with self._dbConnection.get_conn() as session:
            user = session.query(UsuarioModel).find(
                username=username, senha=senha_encriptada).first()

        if not user:
            return None

        return Usuario(
            username=user.username,
            senha=user.senha,
            dadosPessoais=DadosPessoais(
                nome=user.dadosPessoais.nome,
                email=user.dadosPessoais.email,
                telCelular=user.dadosPessoais.telCelular,
                cargo=user.dadosPessoais.cargo)
        )
