from Domain.undoredooperations import Undoredooperations
from Repository.repository import Repository


class Deletealloperation(Undoredooperations):
    def __init__(self,
                 repository: Repository,
                 obiectesterse: list):
        self.repository = repository
        self.obiectesterse = obiectesterse

    def doUndo(self):
        for entitate in self.obiectesterse:
            self.repository.create(entitate)

    def doRedo(self):
        for entitate in self.obiectesterse:
            self.repository.delete(entitate.entity_id)
