from Domain.movie import Movie


from Domain.undoredooperations import Undoredooperations
from Repository.repository import Repository


class Deletealloperation(Undoredooperations):
    def __init__(self,
                 repository1: Repository,
                 repository2: Repository,
                 obiectesterse1: Movie,
                 obiectesterse2: list):
        self.repository1 = repository1
        self.repository2 = repository2
        self.obiectesterse1 = obiectesterse1
        self.obiectesterse2 = obiectesterse2

    def doUndo(self):
        self.repository1.create(self.obiectesterse1)
        for entitate in self.obiectesterse2:
            self.repository2.create(entitate)

    def doRedo(self):
        self.repository1.delete(self.obiectesterse1.entity_id)
        for entitate in self.obiectesterse2:
            self.repository2.delete(entitate.entity_id)
