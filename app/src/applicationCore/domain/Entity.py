from abc import ABCMeta


class Entity(metaclass=ABCMeta):
    """classe base para todas as entidades

    Atributos:
        id: identificador unico da Entidade
    """

    def __init__(self, instance_id: int):
        self._id = instance_id

    @property
    def id(self):
        return self._id
