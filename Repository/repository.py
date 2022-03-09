from typing import Protocol

from Domain.entity import Entity


class Repository(Protocol):
    def read(self, entity_id=None):
        ...

    def create(self, entity: Entity):
        ...

    def update(self, entity: Entity):
        ...

    def delete(self, entity_id):
        ...
