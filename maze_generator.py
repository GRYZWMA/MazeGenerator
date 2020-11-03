# Maze Generator
# https://en.wikipedia.org/wiki/Maze_generation_algorithm
# recursive implementation

import pygame

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

# initialize pygame screen/window
pygame.display.init()
screen_info = pygame.display.Info()
x_axis_screen = screen_info.current_w - 100
y_axis_screen = screen_info.current_h - 100
flags = pygame.RESIZABLE
clock = pygame.time.Clock()
fps_cap = 120
print(x_axis_screen)
print(y_axis_screen)
screen = pygame.display.set_mode((x_axis_screen, y_axis_screen), flags, vsync=1)
pygame.display.set_caption("Recursive Maze Generator v0.01")
# replace this line with graphic: pygame.display.set_icon("icon needed")


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
