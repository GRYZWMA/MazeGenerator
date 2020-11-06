# cell class
class Cell:

    walls = [True, True, True, True]

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def print_cell(self):
        print("Cell is:(" + str(self.x) + "," + str(self.y) + ")")

    def print_walls(self):
        print(" Walls is:(" + str(self.walls[0]) + "," + str(self.walls[1]) + "," + str(self.walls[2]) + "," + str(
            self.walls[3]) + ")")

