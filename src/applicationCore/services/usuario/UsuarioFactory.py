
from src.applicationCore.domain.usuario.Usuario import Usuario
from src.applicationCore.services.usuario.UsuarioBasico import UsuarioBasico


class UsuarioFactory():

    def obterUsuarioBasico(self, usuario: Usuario) -> UsuarioBasico:
        return UsuarioBasico(
            username=usuario.username,
            nome=usuario.dadosPessoais.nome,
            email=usuario.dadosPessoais.email,
            telCelular=usuario.dadosPessoais.telCelular,
            cargo=usuario.dadosPessoais.cargo
        )
