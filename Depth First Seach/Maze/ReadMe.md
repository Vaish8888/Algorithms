Depth First Search Project:

Problem Description:
This repository contains the solution to the LeetCode problem 490 - "Maze." The task is to find a valid path from the starting point to the destination in a given maze. The maze is represented as a 2D grid, where walls are denoted as 1 and open paths as 0. A ball can roll in four cardinal directions (up, down, left, right) until it hits a wall.

Solution Approach:
The solution to the "Maze" problem is implemented using Depth-First Search (DFS) with backtracking. The algorithm explores potential paths in the maze and marks visited cells to prevent cycles. The DFS approach efficiently searches through multiple paths until it reaches the destination or determines that there is no valid path.

Implementation:
The solution is implemented in Python and encapsulated within a function named hasPath(maze, start, destination). The function takes three parameters:

maze: a 2D grid representing the maze.
start: a tuple with the starting point coordinates.
destination: a tuple with the destination point coordinates.

Also find the souce code used to implement the project and you may also refer to the ppt for more detailed information.
