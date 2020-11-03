# MazeGenerator
Recursive implementation: https://en.wikipedia.org/wiki/Maze_generation_algorithm

The depth-first search algorithm of maze generation is frequently implemented using backtracking. This can be described with a following recursive routine:

Given a current cell as a parameter,
Mark the current cell as visited
While the current cell has any unvisited neighbour cells
     Choose one of the unvisited neighbours
     Remove the wall between the current cell and the chosen cell
     Invoke the routine recursively for a chosen cell
