
from datetime import datetime
from typing import List, Optional
from src.applicationCore.domain.reuniao.Convidado import Convidado
from src.applicationCore.domain.reuniao.Lembrete import Lembrete
from src.applicationCore.domain.reuniao.SalaFisica import SalaFisica
from src.applicationCore.domain.reuniao.SalaVirtual import SalaVirtual
from src.applicationCore.domain.reuniao.Status import Status
from src.applicationCore.domain.usuario.DadosPessoais import DadosPessoais
from src.applicationCore.domain.usuario.Usuario import Usuario
from src.adapters.DatabaseConnectionAdapter import DatabaseConnectionAdapter
from src.applicationCore.domain.reuniao.IReuniaoRepository import IReuniaoRepository
from src.applicationCore.domain.reuniao.Reuniao import Reuniao
from src.infrastructure.database.models.ReuniaoModel import ConvidadoModel, ReuniaoModel, SalaEncontroModel


class ReuniaoRepository(IReuniaoRepository):

    def __init__(self, dbConnection: DatabaseConnectionAdapter) -> None:
        super().__init__(dbConnection)

    def save(self, reuniao: Reuniao) -> int:

        reuniaoId = None

        with self._dbConnection.get_conn() as session:
            try:

                salaModel = SalaEncontroModel(
                    nome=reuniao.sala.nome,
                    tipoReuniao=type(
                        reuniao.sala).__name__,
                    numero=reuniao.sala.numero if hasattr(
                        reuniao.sala, 'numero') else None,
                    link=reuniao.sala.link if hasattr(
                        reuniao.sala, 'link') else None)

                session.add(salaModel)
                session.commit()

                model = ReuniaoModel(
                    titulo=reuniao.titulo,
                    pauta=reuniao.pauta,
                    dataInicio=reuniao.dataInicio,
                    dataTermino=reuniao.dataTermino,
                    statusReuniao=reuniao.status.value,
                    lembrete=reuniao.lembrete.value,
                    hostId=reuniao.host.id,
                    sala=salaModel
                )

                session.add(model)
                session.commit()

                convidadosModel = [
                    ConvidadoModel(
                        usuarioId=c.usuario.id,
                        reuniaoId=model.reuniaoId,
                        aceitaReuniao=c.aceitaReuniao)
                    for c in reuniao.convidados]

                session.add_all(convidadosModel)
                session.commit()

                reuniaoId = model.reuniaoId

            except Exception as e:
                session.rollback()
                raise e

        return reuniaoId

    def update(self, reuniao: Reuniao) -> bool:

        with self._dbConnection.get_conn() as session:
            try:

                modelQuery = session.query(ReuniaoModel).\
                    filter(ReuniaoModel.reuniaoId == reuniao.id)

                reuniaoModel = modelQuery.first()

                modelQuery.update({
                    ReuniaoModel.titulo: reuniao.titulo,
                    ReuniaoModel.pauta: reuniao.pauta,
                    ReuniaoModel.dataInicio: reuniao.dataInicio,
                    ReuniaoModel.dataTermino: reuniao.dataTermino,
                    ReuniaoModel.statusReuniao: reuniao.status.value,
                    ReuniaoModel.lembrete: reuniao.lembrete.value
                }, synchronize_session="fetch")

                salaModel = reuniaoModel.sala
                session.query(SalaEncontroModel).\
                    filter(SalaEncontroModel.salaEncontroId == salaModel.salaEncontroId).\
                    update({
                        SalaEncontroModel.nome: reuniao.sala.nome,
                        SalaEncontroModel.tipoReuniao: type(reuniao.sala).__name__,
                        SalaEncontroModel.numero: reuniao.sala.numero if hasattr(
                           reuniao.sala, 'numero') else None,
                        SalaEncontroModel.link: reuniao.sala.link if hasattr(
                            reuniao.sala, 'link') else None}, synchronize_session="fetch")

                convidadosModel = [ConvidadoModel(
                    usuarioId=c.usuario.id,
                    reuniaoId=reuniao.id,
                    aceitaReuniao=c.aceitaReuniao)
                    for c in reuniao.convidados]

                session.query(ConvidadoModel).filter(ConvidadoModel.reuniaoId == reuniao.id).\
                    delete(synchronize_session="fetch")

                session.add_all(convidadosModel)
                session.commit()

            except Exception as e:
                session.rollback()
                raise e

    def delete(self, reuniao: Reuniao) -> bool:
        raise NotImplementedError

    def findById(self, reuniaoId: int) -> Optional[Reuniao]:

        with self._dbConnection.get_conn() as session:

            model: ReuniaoModel = session.query(ReuniaoModel).filter_by(
                reuniaoId=reuniaoId).one_or_none()

            if not model:
                return None

            host = Usuario(
                usuarioId=model.host.usuarioId,
                username=model.host.username,
                senha="",
                dadosPessoais=DadosPessoais(
                    nome=model.host.dadosPessoais.nome,
                    email=model.host.dadosPessoais.email,
                    telCelular=model.host.dadosPessoais.telCelular,
                    cargo=model.host.dadosPessoais.cargo))

            convidados = [Convidado(
                aceitaReuniao=c.aceitaReuniao,
                usuario=Usuario(
                    usuarioId=c.usuario.usuarioId,
                    username=c.usuario.username,
                    senha=c.usuario.senha,
                    dadosPessoais=DadosPessoais(
                        nome=c.usuario.dadosPessoais.nome,
                        email=c.usuario.dadosPessoais.email,
                        telCelular=c.usuario.dadosPessoais.telCelular,
                        cargo=c.usuario.dadosPessoais.cargo)
                )) for c in model.convidados]

            sala = None

            if model.sala.tipoReuniao == SalaVirtual.__name__:
                sala = SalaVirtual(
                    nome=model.sala.nome,
                    link=model.sala.link)
            else:
                sala = SalaFisica(
                    nome=model.sala.nome,
                    numero=model.sala.numero)

            return Reuniao(
                reuniaoId=model.reuniaoId,
                titulo=model.titulo,
                pauta=model.pauta,
                dataInicio=model.dataInicio,
                dataTermino=model.dataTermino,
                host=host,
                sala=sala,
                status=Status(model.statusReuniao),
                lembrete=Lembrete(model.lembrete),
                convidados=convidados)

    def findAllBetweenDataInicioAndDataTerminoFromUsuario(self, dataInicio: datetime,
                                                          dataTermino: datetime, usuarioId: int) -> List[Reuniao]:
        raise NotImplementedError
