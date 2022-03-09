from Domain.entity import Entity
from Domain.undoredooperations import Undoredooperations
from Repository.repository import Repository


class Addoperation(Undoredooperations):
    def __init__(self,
                 repository: Repository,
                 obiectadaugat: Entity):
        self.repository = repository
        self.obiectadaugat = obiectadaugat

    def doUndo(self):
        self.repository.delete(self.obiectadaugat.entity_id)

    def doRedo(self):
        self.repository.create(self.obiectadaugat)
