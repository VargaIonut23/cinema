import jsonpickle

from Domain.entity import Entity
from Repository.repository_in_memory import RepositoryInMemory


class RepositoryJson(RepositoryInMemory):
    def __init__(self, filename):
        super().__init__()
        self.filename = filename

    def __readFile(self):
        try:
            with open(self.filename, "r") as f:
                return jsonpickle.loads(f.read())
        except Exception:
            return {}

    def __writeFile(self):
        with open(self.filename, "w") as f:
            f.write(jsonpickle.dumps(self.entities, indent=2))

    def read(self, entity_id=None):
        self.entities = self.__readFile()
        return super().read(entity_id)

    def create(self, entity: Entity):
        self.entities = self.__readFile()
        super().create(entity)
        self.__writeFile()

    def update(self, entity: Entity):
        self.entities = self.__readFile()
        super().update(entity)
        self.__writeFile()

    def delete(self, entity_id):
        self.entities = self.__readFile()
        super().delete(entity_id)
        self.__writeFile()
