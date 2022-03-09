from Domain.entity import Entity
from Domain.undoredooperations import Undoredooperations
from Repository.repository import Repository


class Deleteoperation(Undoredooperations):
    def __init__(self,
                 repository: Repository,
                 obiectsters: Entity):
        self.repository = repository
        self.obiectsters = obiectsters

    def doUndo(self):
        self.repository.create(self.obiectsters)

    def doRedo(self):
        self.repository.delete(self.obiectsters.entity_id)
