
from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import declarative_base, relationship

from src.infrastructure.database.models.UsuarioModel import UsuarioModel

Base = declarative_base()


class SalaEncontroModel(Base):

    __tablename__ = "SalaEncontro"

    salaEncontroId = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)
    tipoReuniao = Column(String(25), nullable=False)
    numero = Column(Integer, nullable=True)
    link = Column(String, nullable=True)


class ConvidadoModel(Base):

    __tablename__ = "Convidado"

    convidadoId = Column(Integer, primary_key=True)
    usuarioId = Column(Integer, ForeignKey(UsuarioModel.usuarioId))
    reuniaoId = Column(Integer, ForeignKey('Reunioes.reuniaoId'))
    aceitaReuniao = Column(Boolean, default=True)
    usuario = relationship(UsuarioModel, backref="Convidado", lazy="joined")


class ReuniaoModel(Base):

    __tablename__ = "Reunioes"

    reuniaoId = Column(Integer, primary_key=True)
    titulo = Column(String, nullable=False)
    pauta = Column(String, nullable=False)
    dataInicio = Column(DateTime, nullable=False)
    dataTermino = Column(DateTime, nullable=False)
    statusReuniao = Column(String, nullable=False)
    lembrete = Column(Integer, nullable=False)
    hostId = Column(Integer, ForeignKey(UsuarioModel.usuarioId))
    host = relationship(UsuarioModel, backref="Reunioes", lazy="joined")
    salaEncontroId = Column(Integer, ForeignKey('SalaEncontro.salaEncontroId'))
    convidados = relationship(
        "ConvidadoModel", backref="Reunioes", lazy="joined")
    sala = relationship(
        "SalaEncontroModel", backref="Reunioes", uselist=False, lazy="joined")
