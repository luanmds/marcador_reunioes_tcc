
from src.applicationCore.domain.reuniao.Convidado import Convidado
from src.adapters.NotifierAdapter import NotifierAdapter


class EmailNotifier(NotifierAdapter):

    def __init__(self, mensagem: str):
        super().__init__(mensagem)

    def enviarNotificacao(self, remetente: Convidado):
        logs = f'''
        ####### 
            Envio de E-mail para o Convidado: {remetente.usuario.username}
        ####### '''

        print(logs)
