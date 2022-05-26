
from src.applicationCore.domain.reuniao.Convidado import Convidado
from src.adapters.NotifierAdapter import NotifierAdapter


class SMSNotifier(NotifierAdapter):

    def __init__(self, mensagem: str):
        super().__init__(mensagem)

    def enviarNotificacao(self, remetente: Convidado):
        logs = f'''
        ####### 
            Envio de SMS para o Tel. Celular do Convidado: {remetente.usuario.username}
        ####### '''

        print(logs)
