from garbage import Garbage


class PlasticGarbage(Garbage):

    def __init__(self, name, is_clean):
        self.is_clean = is_clean
        Garbage.__init__(self, name)

    def clean(self):
        self.is_clean = True
