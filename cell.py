# cell class
class Cell:

    def __init__(self, i, j):
        self.i = i
        self.j = j

    def print_cell(self):
        print("Cell is:(" + str(self.i) + "," + str(self.j) + ")")
