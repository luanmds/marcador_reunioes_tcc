
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Boolean
from sqlalchemy.orm import declarative_base, relationship, backref

Base = declarative_base()


class SalaEncontroModel(Base):

    __tablename__ = "SalaEncontro"

    salaEncontroId = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)
    tipoReuniao = Column(String(25), nullable=False)
    numero = Column(Integer, nullable=True)
    link = Column(String, nullable=True)
    reuniaoId = Column(Integer, ForeignKey('Reunioes.reuniaoId'))


class ConvidadoModel(Base):

    __tablename__ = "Convidado"

    convidadoId = Column(Integer, primary_key=True)
    usuarioId = Column(Integer, ForeignKey('Usuarios.usuarioId'))
    reuniaoId = Column(Integer, ForeignKey('Reunioes.usuarioId'))
    aceitaReuniao = Column(Boolean, default=True)


class ReuniaoModel(Base):

    __tablename__ = "Reunioes"

    reuniaoId = Column(Integer, primary_key=True)
    titulo = Column(String, nullable=False)
    pauta = Column(String, nullable=False)
    dataInicio = Column(DateTime, nullable=False)
    dataTermino = Column(DateTime, nullable=False)
    status = Column(String, nullable=False)
    lembrete = Column(Integer, nullable=False)
    host = Column(Integer, ForeignKey('Usuarios.usuarioId'))
    convidados = relationship("ConvidadoModel", backref="Reunioes")
    sala = relationship(
        "SalaEncontroModel", backref="Reunioes", uselist=False)
