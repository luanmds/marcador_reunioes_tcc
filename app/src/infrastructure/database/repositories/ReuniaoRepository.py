
from datetime import datetime
from typing import List, Optional
from src.adapters.DatabaseConnectionAdapter import DatabaseConnectionAdapter
from src.applicationCore.domain.reuniao.IReuniaoRepository import IReuniaoRepository
from src.applicationCore.domain.reuniao.Reuniao import Reuniao
from src.infrastructure.database.models.ReuniaoModel import ConvidadoModel, ReuniaoModel, SalaEncontroModel


class ReuniaoRepository(IReuniaoRepository):

    def __init__(self, dbConnection: DatabaseConnectionAdapter) -> None:
        super().__init__(dbConnection)

    def save(self, reuniao: Reuniao) -> int:

        salaModel = SalaEncontroModel(
            nome=reuniao.sala.nome,
            tipoReuniao=reuniao.sala.__class__,
            numero=reuniao.sala.numero if reuniao.sala.numero else None,
            link=reuniao.sala.link if reuniao.sala.link else None
        )

        convidadosModel = [
            ConvidadoModel(
                usuarioId=c.usuario.id,
                aceitaReuniao=c.aceitaReuniao)
            for c in reuniao.convidados]

        model = ReuniaoModel(
            titulo=reuniao.titulo,
            pauta=reuniao.pauta,
            dataInicio=reuniao.dataInicio,
            dataTermino=reuniao.dataTermino,
            status=reuniao.status.value,
            lembrete=reuniao.lembrete.value,
            host=reuniao.host.id,
            sala=salaModel,
            convidados=convidadosModel
        )

        with self._dbConnection.get_conn() as session:
            session.add(model)
            session.commit()

        return model.reuniaoId

    def update(self, reuniao: Reuniao) -> bool:
        raise NotImplementedError

    def delete(self, reuniao: Reuniao) -> bool:
        raise NotImplementedError

    def findById(self, reuniaoId: int) -> Optional[Reuniao]:
        raise NotImplementedError

    def findAllBetweenDataInicioAndDataTerminoFromUsuario(self, dataInicio: datetime,
                                                          dataTermino: datetime, usuarioId: int) -> List[Reuniao]:
        raise NotImplementedError
