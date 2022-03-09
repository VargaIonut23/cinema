from Domain.undoredooperations import Undoredooperations
from Repository.repository import Repository


class Incrementarepuncteoperation(Undoredooperations):
    def __init__(self,
                 repository: Repository,
                 obiectesterse: list,
                 puncte: int):
        self.repository = repository
        self.obiectesterse = obiectesterse
        self.puncte = puncte

    def doUndo(self):
        for entitate in self.obiectesterse:
            entitate.PuncteAcumulate = entitate.PuncteAcumulate - self.puncte
            self.repository.update(entitate)

    def doRedo(self):
        for entitate in self.obiectesterse:
            entitate.PuncteAcumulate = entitate.PuncteAcumulate + self.puncte
            self.repository.update(entitate)
