# Maze Generator
# https://en.wikipedia.org/wiki/Maze_generation_algorithm
# recursive implementation

import pygame
import cell
import time
import random

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
grid_points = []
grid = []
stack = []
visited = []

# initialize pygame screen/window
pygame.display.init()
screen_info = pygame.display.Info()
x_axis_screen = screen_info.current_w - 100
y_axis_screen = screen_info.current_h - 100
x_axis_screen = 1000
y_axis_screen = 1000
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
first_grid_x = int((x_axis_screen * .2) / 2)
first_grid_y = int((y_axis_screen * .2) / 2)
line_width = 1
border_width = 1

cell_x = 50
cell_y = 0
for j in range(int((y_axis_screen / 50) - 2)):
    cell_x = 50
    cell_y = cell_y + 50
    for i in range((int(x_axis_screen / 50) - 2)):
        create_cell = cell.Cell(cell_x, cell_y)
        grid_points.append(create_cell)
        grid.append((create_cell.x, create_cell.y))
        pygame.draw.circle(screen, color_red, (cell_x, cell_y), 1)
        pygame.display.update()
        cell_x = cell_x + 50
        # time.sleep(.1)


def draw_cell(dc1, dc2, d_cell=[]):
    # time.sleep(.1)
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


def starting_cell(x, y):
    pygame.draw.rect(screen, color_blue, (x + 1, y + 1, cell_width - 2, cell_width - 2), 0)  # draw a single width cell
    pygame.display.update()


def draw_right(x, y):
    pygame.draw.rect(screen, color_purple, (x + 1, y + 1, (cell_width * 2) - 1, cell_width - 1), 0)
    pygame.display.update()


def draw_left(x, y):
    pygame.draw.rect(screen, color_purple, (x - cell_width + 1, y + 1, (cell_width * 2 - 1), cell_width - 1), 0)
    pygame.display.update()


def draw_up(x, y):
    pygame.draw.rect(screen, color_purple, (x + 1, y - cell_width + 1, cell_width - 1, (cell_width * 2) - 1), 0)
    pygame.display.update()


def draw_down(x, y):
    pygame.draw.rect(screen, color_purple, (x + 1, y + 1, cell_width - 1, (cell_width * 2) - 1), 0)
    pygame.display.update()


def cell_reset(x, y):
    pygame.draw.rect(screen, color_purple, (x + 1, y + 1, cell_width - 2, cell_width - 2), 0)
    pygame.display.update()


def draw_maze(x, y):
    print(grid)
    starting_cell(x, y)
    stack.append((x, y))
    visited.append((x, y))
    while len(stack) > 0:
        print(str(x) + "," + str(y))
        print(len(stack))
        time.sleep(.1)
        cell_list = []
        print(str(x + cell_width) + "," + str(y))
        if (x + cell_width, y) not in visited and (x + cell_width, y) in grid:
            cell_list.append("right")
        if (x - cell_width, y) not in visited and (x - cell_width, y) in grid:
            cell_list.append("left")
        if (x, y + cell_width) not in visited and (x, y + cell_width) in grid:
            cell_list.append("down")
        if (x, y - cell_width) not in visited and (x, y - cell_width) in grid:
            cell_list.append("up")
        if len(cell_list) > 0:
            chosen_cell = (random.choice(cell_list))
            print("here")
            if chosen_cell == "right":
                draw_right(x, y)
                x = x + cell_width
                visited.append((x, y))
                stack.append((x, y))
            elif chosen_cell == "left":
                draw_left(x, y)
                x = x - cell_width
                visited.append((x, y))
                stack.append((x, y))
            elif chosen_cell == "up":
                draw_up(x, y)
                y = y - cell_width
                visited.append((x, y))
                stack.append((x, y))
            elif chosen_cell == "down":
                draw_down(x, y)
                y = y + cell_width
                visited.append((x, y))
                stack.append((x, y))
        else:
            x, y = stack.pop()
            starting_cell(x, y)
            time.sleep(.1)
            cell_reset(x, y)


for k in grid_points:
    k.print_cell()
    # k.print_walls()
    draw_cell(k.x, k.y, k.walls)

first_grid_x = int((x_axis_screen * .2) / 2)
first_grid_y = int((y_axis_screen * .2) / 2)
print("grid x" + str(first_grid_x))
print("grid y" + str(first_grid_y))
draw_maze(50, 50)

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
