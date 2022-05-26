from sqlalchemy import or_
from typing import List, Optional

from src.infrastructure.database.DbSqlConnection import DbSqlConnection

from src.applicationCore.domain.usuario.DadosPessoais import DadosPessoais
from src.applicationCore.domain.usuario.IUsuarioRepository import \
    IUsuarioRepository
from src.applicationCore.domain.usuario.Usuario import Usuario
from src.infrastructure.database.models.UsuarioModel import DadosPessoaisModel, UsuarioModel


class UsuarioRepository(IUsuarioRepository):

    def __init__(self, dbConnection: DbSqlConnection) -> None:
        super().__init__(dbConnection)

    def findById(self, usuarioId: int) -> Optional[Usuario]:
        raise NotImplementedError

    def findByNomeOrUsername(self, palavras: List[str]) -> List[Usuario]:

        with self._dbConnection.get_conn() as session:
            users = session.query(UsuarioModel).where(
                or_(UsuarioModel.username.in_(palavras), DadosPessoaisModel.nome.in_(palavras)))

            if not users:
                return []

            return [Usuario(
                usuarioId=user.usuarioId,
                username=user.username,
                senha=user.senha,
                dadosPessoais=DadosPessoais(
                    nome=user.dadosPessoais.nome,
                    email=user.dadosPessoais.email,
                    telCelular=user.dadosPessoais.telCelular,
                    cargo=user.dadosPessoais.cargo)
            ) for user in users]

    def findByUsername(self, username: str) -> Optional[Usuario]:

        with self._dbConnection.get_conn() as session:
            user = session.query(UsuarioModel).filter_by(
                username=username).one_or_none()

            if not user:
                return None

            usuario = Usuario(
                usuarioId=user.usuarioId,
                username=user.username,
                senha=user.senha,
                dadosPessoais=DadosPessoais(
                    nome=user.dadosPessoais.nome,
                    email=user.dadosPessoais.email,
                    telCelular=user.dadosPessoais.telCelular,
                    cargo=user.dadosPessoais.cargo)
            )

            return usuario
