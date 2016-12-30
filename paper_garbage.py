from garbage import Garbage


class PaperGarbage(Garbage):

    def __init__(self, name, is_squeezed):
        self.is_squeezed = is_squeezed
        Garbage.__init__(self, name)

    def squeeze(self):
        self.is_squeezed = True
