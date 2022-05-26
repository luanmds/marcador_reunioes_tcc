import os

from dependency_injector import containers, providers
from src.applicationCore.services.reuniao.ReuniaoService import ReuniaoService
from src.infrastructure.adaptadores.EmailNotifier import EmailNotifier
from src.infrastructure.adaptadores.SMSNotifier import SMSNotifier
from src.applicationCore.services.usuario.UsuarioService import UsuarioService
from src.infrastructure.database.DbSqlConnection import DbSqlConnection
from src.infrastructure.database.repositories.ReuniaoRepository import \
    ReuniaoRepository
from src.infrastructure.database.repositories.UsuarioRepository import \
    UsuarioRepository


class Dependencies(containers.DeclarativeContainer):

    config = providers.Configuration()

    # database connection
    db_conn = providers.Singleton(
        DbSqlConnection,
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASS'),
        host=os.getenv('DB_HOST'),
        database=os.getenv('DB_SCHEMA'))

    # repositories
    _usuarioRepository = providers.Singleton(
        UsuarioRepository, dbConnection=db_conn)
    _reuniaoRepository = providers.Singleton(
        ReuniaoRepository, dbConnection=db_conn)

    # adapters
    emailNotifier = providers.Singleton(
        EmailNotifier,
        mensagem="Você está convidado para a reunião")

    smsNotifier = providers.Singleton(
        SMSNotifier,
        mensagem="Você está convidado para a reunião")

    # services
    usuarioService = providers.Factory(
        UsuarioService,
        usuarioRepo=_usuarioRepository)

    reuniaoService = providers.Factory(
        ReuniaoService,
        reuniaoRepo=_reuniaoRepository,
        usuarioRepo=_usuarioRepository,
        notificadores=providers.List(emailNotifier, smsNotifier))
