from Domain import movie
from Domain.entity import Entity
from Repository.repository import Repository


class RepositoryInMemory(Repository):
    def __init__(self):
        self.entities = {}

    def read(self, entity_id=None):
        if entity_id is None:
            return list(self.entities.values())

        if entity_id in self.entities:
            return self.entities[entity_id]
        else:
            return None

    def create(self, entity: Entity):
        if self.read(entity.entity_id) is not None:
            raise KeyError("Exista deja o entitate cu id-ul dat!")
        self.entities[entity.entity_id] = entity

    def update(self, entity: Entity):
        if self.read(entity.entity_id) is None:
            raise KeyError("Nu exista o entitate cu id-ul dat!")
        self.entities[entity.entity_id] = entity

    def delete(self, id_entity):
        if self.read(id_entity) is None:
            raise KeyError("Nu exista o entitate cu id-ul dat!")
        del self.entities[id_entity]
