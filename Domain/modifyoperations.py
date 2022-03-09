from Domain.entity import Entity
from Domain.undoredooperations import Undoredooperations
from Repository.repository import Repository


class Modifyoperation(Undoredooperations):
    def __init__(self,
                 repository: Repository,
                 obiectnou: Entity,
                 obiectvechi: Entity):
        self.repository = repository
        self.obiectnou = obiectnou
        self.obiectvechi = obiectvechi

    def doUndo(self):
        self.repository.update(self.obiectvechi)

    def doRedo(self):
        self.repository.update(self.obiectnou)
