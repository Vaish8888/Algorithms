## Problem Description

You are given an `m x n` matrix `maze` representing an environment. The maze has an entrance and an exit, both located on the border of the matrix. You can move in any of the four cardinal directions: up, down, left, or right. You cannot move diagonally or outside the boundary of the maze.

The task is to determine if you can reach the exit from the entrance using the BFS (Breadth-First Search) approach. Return `True` if you can reach the exit, otherwise, return `False`.

### Example

```
Input: 
maze = [
    [0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0],
    [1, 1, 0, 1, 1],
    [0, 0, 0, 0, 0]
]
start = (0, 4)
destination = (4, 4)

Output: True
```

## Solution Approach

We will use the Breadth-First Search (BFS) algorithm to explore the maze starting from the entrance. The BFS algorithm explores all possible directions in a level-by-level manner until it reaches the exit or has explored all reachable cells.

1. We begin by initializing a queue with the starting position (entrance) `(start)`.
2. We also initialize a set `visited` to keep track of cells we have visited to avoid revisiting them.
3. While the queue is not empty, we perform the following steps:
   - Dequeue a cell from the queue and mark it as visited.
   - Check if the dequeued cell is the destination. If yes, return `True` as we have found a path to the exit.
   - Otherwise, explore all possible directions (up, down, left, right) from the current cell.
   - For each valid neighbor cell, add it to the queue if it has not been visited before.
   - Repeat until the queue is empty or the destination is found.

If the BFS algorithm completes without finding the destination, we return `False`, indicating that there is no valid path from the entrance to the exit.

Example Usage:

```python
maze = [
    [0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0],
    [1, 1, 0, 1, 1],
    [0, 0, 0, 0, 0]
]
start = (0, 4)
destination = (4, 4)

print(hasPath(maze, start, destination))  # Output: True
```

## Time Complexity

The time complexity of the BFS approach for solving this problem is O(m * n) since, in the worst case, we may visit all cells in the maze once.

## Space Complexity

The space complexity of the BFS approach is O(m * n) as we may need to store all cells in the `visited` set in the worst case.

---

I hope this README document helps you understand the problem and the solution approach clearly. 
