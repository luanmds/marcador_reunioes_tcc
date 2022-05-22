
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class UsuarioModel(Base):

    __tablename__ = "Usuarios"

    usuarioId = Column(Integer, primary_key=True)
    username = Column(String(25), unique=True, nullable=False)
    senha = Column(String(200), nullable=False)
    dadosPessoais = relationship(
        "DadosPessoaisModel", backref="Usuarios", uselist=False)


class DadosPessoaisModel(Base):

    __tablename__ = "DadosPessoais"

    dadosPessoaisId = Column(Integer, primary_key=True)
    nome = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False)
    telCelular = Column(String(12), nullable=False)
    cargo = Column(String(35), nullable=False)
    usuarioId = Column(Integer, ForeignKey('Usuarios.usuarioId'))
