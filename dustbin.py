from garbage import Garbage
from paper_garbage import PaperGarbage
from plastic_garbage import PlasticGarbage
from dustbin_content_error import DustbinContentError


class Dustbin:

    def __init__(self, color):
        self.color = color
        self.paper_content = []
        self.plastic_content = []
        self.house_waste_content = []

    def throw_out_garbage(self, garbage):
        if type(garbage) == PlasticGarbage and garbage.is_clean:
            self.plastic_content.append(garbage.name)

        elif type(garbage) == PaperGarbage and garbage.is_squeezed:
            self.paper_content.append(garbage.name)

        elif type(garbage) == Garbage:
            self.house_waste_content.append(garbage.name)

        else:
            raise DustbinContentError

    def empty_contents(self):
        self.plastic_content.clear()
        self.paper_content.clear()
        self.house_waste_content.clear()
