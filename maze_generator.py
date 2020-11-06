# Maze Generator
# https://en.wikipedia.org/wiki/Maze_generation_algorithm
# recursive implementation

import pygame
import cell
import time

# -------color variables---------
color_black = [0, 0, 0]
color_white = [255, 255, 255]
color_red = [255, 0, 0]
color_green = [0, 255, 0]
color_blue = [0, 0, 255]
color_yellow = [255, 255, 0]
color_cyan = [0, 255, 255]
color_purple = [255, 0, 255]

# -------pygame variables---------
# Screen Setup
x_axis_screen = 0
y_axis_screen = 0
running = True
cell_width = 50
cols = x_axis_screen / cell_width
rows = y_axis_screen / cell_width
grid = []

# initialize pygame screen/window
pygame.display.init()
screen_info = pygame.display.Info()
x_axis_screen = screen_info.current_w - 100
y_axis_screen = screen_info.current_h - 100
x_axis_screen = 500
y_axis_screen = 500
flags = 0
clock = pygame.time.Clock()
fps_cap = 120
print(x_axis_screen)
print(y_axis_screen)
screen = pygame.display.set_mode((x_axis_screen, x_axis_screen), flags, vsync=1)
pygame.display.set_caption("Recursive Maze Generator v0.01")
program_icon = pygame.image.load('Maze.png')
pygame.display.set_icon(program_icon)

# create initial grid in middle of screen
first_grid_x = (x_axis_screen * .2) / 2
first_grid_y = (y_axis_screen * .2) / 2
line_width = 1
border_width = 1

cell_x = 50
cell_y = 0
for j in range(int((y_axis_screen / 50) - 2)):
    cell_x = 50
    cell_y = cell_y + 50
    for i in range((int(x_axis_screen / 50) - 2)):
        create_cell = cell.Cell(cell_x, cell_y)
        grid.append(create_cell)
        pygame.draw.circle(screen, color_red, (cell_x, cell_y), 1)
        pygame.display.update()
        cell_x = cell_x + 50
        time.sleep(.1)


def draw_cell(dc1, dc2, d_cell=[]):
    time.sleep(.1)
    if d_cell[0]:  # top
        pygame.draw.line(screen, color_white, (dc1, dc2), (dc1 + cell_width, dc2), 1)
        pygame.display.update()
    if d_cell[1]:  # left
        pygame.draw.line(screen, color_white, (dc1, dc2), (dc1, dc2 + cell_width), 1)
        pygame.display.update()
    if d_cell[2]:  # right
        pygame.draw.line(screen, color_white, (dc1 + cell_width, dc2), (dc1 + cell_width, dc2 + cell_width), 1)
        pygame.display.update()
    if d_cell[3]:  # bottom
        pygame.draw.line(screen, color_white, (dc1, dc2 + cell_width), (dc1 + cell_width, dc2 + cell_width), 1)
        pygame.display.update()


for k in grid:
    k.print_cell()
    k.print_walls()
    draw_cell(k.x, k.y, k.walls)

# maze generator logic
while running:
    clock.tick(fps_cap)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()

pygame.quit()
