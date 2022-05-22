
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
from sqlalchemy import create_engine

engine = create_engine("mysql+mysqlconnector://root:admin123@localhost:3306")

# engine.execute('CREATE DATABASE marcadorReuniaoDB')
engine.execute('USE marcadorReuniaoDB')


Base = declarative_base()


class UsuarioModel(Base):

    __tablename__ = "Usuarios"

    usuarioId = Column(Integer, primary_key=True)
    username = Column(String(25), unique=True, nullable=False)
    senha = Column(String(255), nullable=False)
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

# UsuarioModel.__table__.drop(engine)
# DadosPessoaisModel.__table__.drop(engine)

# Base.metadata.create_all(engine)

dbSession = sessionmaker(bind=engine)
session = dbSession()


dadosPessoais = DadosPessoaisModel(
    nome="Luan Mello",
    email="luan.m@gmail.com",
    telCelular="21989248235",
    cargo="Arquiteto de TI"
)

user = UsuarioModel(
    username="luan.m",
    senha="080297",
    dadosPessoais=dadosPessoais)

session.add_all([user, dadosPessoais])
session.commit()

print(user.usuarioId)
