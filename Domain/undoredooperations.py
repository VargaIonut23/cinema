from abc import ABC


class Undoredooperations (ABC):
    def doUndo(self):
        ...

    def doRedo(self):
        ...
