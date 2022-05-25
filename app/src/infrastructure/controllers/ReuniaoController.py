import dataclasses
import os
from datetime import datetime, timedelta
from enum import Enum

from src.infrastructure.controllers.ReuniaoSchema import (
    ReuniaoSchema, SalaEncontroSchema)
from dependency_injector.wiring import Provide, inject
from flask import request
from flask_restx import Namespace, Resource, fields
from src.applicationCore.domain.reuniao.Lembrete import Lembrete
from src.applicationCore.domain.reuniao.SalaFisica import SalaFisica
from src.applicationCore.domain.reuniao.SalaVirtual import SalaVirtual
from src.applicationCore.services.exceptions.ReuniaoException import (
    ConvidadoNotFound, ReuniaoCancelada, ReuniaoNotFound)
from src.applicationCore.services.reuniao.ReuniaoDTO import ReuniaoDTO
from src.applicationCore.services.reuniao.ReuniaoService import ReuniaoService
from src.applicationCore.services.usuario.UsuarioBasico import UsuarioBasico
from src.infrastructure.Dependencies import Dependencies
from src.utils.token_required import token_required

api = Namespace(
    'reuniao', description='Operações envolvendo CRUD de Reuniões na aplicação')


class TipoSala(Enum):
    VIRTUAL = 'VIRTUAL'
    FISICA = 'FISICA'


class DateTimeCustom(fields.DateTime):
    __schema_format__ = "datetime"
    __schema_example__ = "2022-01-01 00:00"

    def parse(self, value):
        if value is None:
            return None
        try:
            return datetime.strptime(value, "%Y-%m-%d %H:%M")
        except ValueError as e:
            raise ValueError("Unsupported format for Datetime") from e

    def format(self, value: datetime):
        try:
            value = self.parse(value)
            return value.isoformat(timespec="seconds")
        except ValueError as e:
            raise fields.MarshallingError(e)


reuniao_fields = api.model('reuniao', {
    'titulo': fields.String(required=True, description='Título da Reunião'),
    'pauta': fields.String(required=True, description='Pauta/Resumo da Reunião'),
    'dataInicio': DateTimeCustom(required=True, description='Data e Hora do Começo da Reunião'),
    'dataTermino': DateTimeCustom(required=True, description='Data e Hora do Término da Reunião'),
    'tipoSala': fields.String(required=True, description="Sala onde ocorrerá a Reunião", enum=TipoSala._member_names_),
    'nomeSala': fields.String(required=True, description="Nome da Sala da Reunião"),
    'linkSalaVirtual': fields.String(description="Link da Sala Virtual. Apenas se tipoSala = VIRTUAL"),
    'numeroSalaFisica': fields.Integer(description="Número da Sala Física. Apenas se tipoSala = FISICA"),
    'tempoLembrete': fields.String(required=True, description="Tempo para o Lembrete antes do horário de início da Reunião", enum=Lembrete._member_names_),
    'convidadosUsernames': fields.List(fields.String, required=True, description="Usernames dos Convidados para participar da Reunião. Devem ser separados por espaço em branco.")
})


@api.route('/')
class ReuniaoCreate(Resource):

    @api.doc('Criar Reunião', security='apikey')
    @api.expect(reuniao_fields, validate=True)
    @token_required
    @inject
    def post(self, current_user: UsuarioBasico, reuniaoService: ReuniaoService = Provide[Dependencies.reuniaoService]):

        post_data = request.json

        reuniaoService._usuarioLogado = current_user

        tipo_sala = TipoSala(post_data['tipoSala'])
        sala_encontro = None

        if tipo_sala == TipoSala.VIRTUAL:
            sala_encontro = SalaVirtual(
                nome=post_data['nomeSala'], link=post_data['linkSalaVirtual'])
        elif tipo_sala == TipoSala.FISICA:
            sala_encontro = SalaFisica(
                nome=post_data['nomeSala'], numero=post_data['numeroSalaFisica'])

        dto = ReuniaoDTO(
            titulo=post_data['titulo'],
            pauta=post_data['pauta'],
            dataInicio=datetime.strptime(
                post_data['dataInicio'], '%Y-%m-%d %H:%M'),
            dataFim=datetime.strptime(
                post_data['dataTermino'], '%Y-%m-%d %H:%M'),
            local=sala_encontro,
            lembrete=Lembrete[post_data['tempoLembrete']],
            convidadosUsernames=post_data['convidadosUsernames'])

        reuniao_id = reuniaoService.criarReuniao(reuniaoDto=dto)

        return {
            "message": f"Reunião marcada com sucesso",
            "status": "success",
            "data": {
                "reuniaoId": reuniao_id
            }
        }, 201


@api.route('/<int:id>')
@api.param('id', 'Identificador da Reunião')
class Reuniao(Resource):

    @api.doc('Obter Reunião', security='apikey')
    @token_required
    @inject
    def get(self, current_user: UsuarioBasico, id, reuniaoService: ReuniaoService = Provide[Dependencies.reuniaoService]):

        reuniaoService._usuarioLogado = current_user

        try:
            reuniao = reuniaoService.buscaReuniaoPorId(reuniaoId=id)

            reuniaoSchema = ReuniaoSchema()

            return {
                "message": f"Reunião buscada com sucesso",
                "status": "success",
                "data": {
                    "reuniao": reuniaoSchema.dump(reuniao.__dict__)
                }
            }, 200

        except ReuniaoNotFound as e:
            return {
                "message": e.message,
                "status": "error"
            }, 404

    @api.doc('Atualizar Reunião', security='apikey')
    @api.expect(reuniao_fields, validate=True)
    @token_required
    @inject
    def put(self, current_user: UsuarioBasico, id, reuniaoService: ReuniaoService = Provide[Dependencies.reuniaoService]):

        put_data = request.json

        reuniaoService._usuarioLogado = current_user

        try:
            tipo_sala = TipoSala(put_data['tipoSala'])
            sala_encontro = None

            if tipo_sala == TipoSala.VIRTUAL:
                sala_encontro = SalaVirtual(
                    nome=put_data['nomeSala'], link=put_data['linkSalaVirtual'])
            elif tipo_sala == TipoSala.FISICA:
                sala_encontro = SalaFisica(
                    nome=put_data['nomeSala'], numero=put_data['numeroSalaFisica'])

            dto = ReuniaoDTO(
                reuniaoId=id,
                titulo=put_data['titulo'],
                pauta=put_data['pauta'],
                dataInicio=put_data['dataInicio'],
                dataFim=put_data['dataTermino'],
                local=sala_encontro,
                lembrete=Lembrete[put_data['tempoLembrete']],
                convidadosUsernames=put_data['convidadosUsernames'])

            reuniao_id = reuniaoService.atualizarReuniao(reuniaoDto=dto)

            return {
                "message": f"Reunião atualizada com sucesso",
                "status": "success"
            }, 202

        except ReuniaoNotFound or ConvidadoNotFound as e:
            return {
                "message": e.message,
                "status": "error"
            }, 404
        except ReuniaoCancelada as e:
            return {
                "message": e.message,
                "status": "error"
            }, 400

    @api.doc('Cancelar Reunião', security='apikey')
    @token_required
    @inject
    def delete(self, current_user: UsuarioBasico, id, reuniaoService: ReuniaoService = Provide[Dependencies.reuniaoService]):

        reuniaoService._usuarioLogado = current_user

        try:
            reuniaoService.cancelarReuniao(reuniaoId=id)

            return {
                "message": "Reunião cancelada com sucesso",
                "status": "success"
            }, 202

        except ReuniaoNotFound as e:
            return {
                "message": e.message,
                "status": "error"
            }, 404
        except ReuniaoCancelada as e:
            return {
                "message": e.message,
                "status": "error"
            }, 400
