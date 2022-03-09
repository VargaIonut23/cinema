from Domain.undoredooperations import Undoredooperations


class Undoredoservice:
    def __init__(self):
        self.undooperation = []
        self.redooperation = []

    def adaugaOperatie(self, undoredooperations: Undoredooperations):
        self.undooperation.append(undoredooperations)
        self.redooperation.append(undoredooperations)

    def undo(self):
        if self.undooperation:
            lastundooperation = self.undooperation.pop()
            self.redooperation.append(lastundooperation)
            lastundooperation.doUndo()
        else:
            print('Nu se poate face undo')

    def redo(self):
        if self.redooperation:
            lastredooperation = self.redooperation.pop()
            self.undooperation.append(lastredooperation)
            lastredooperation.doRedo()
        else:
            print('Nu se poate face redo')
