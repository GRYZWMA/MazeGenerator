# cell class
class Cell:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def print_cell(self):
        print("Cell is:(" + str(self.x) + "," + str(self.y) + ")")