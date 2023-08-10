from collections import deque
def hasPath(maze, start, destination):
    if not maze or not maze[0]:
        return False
    m, n = len(maze), len(maze[0])
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # right, down, left, up
    queue = deque([start])
    visited = set()
    while queue:
        x, y = queue.popleft()
        if (x, y) == destination:
            return True
        if (x, y) in visited:
            continue
        visited.add((x, y))
        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy
            # Keep rolling in the current direction until hitting a wall
            while 0 <= new_x < m and 0 <= new_y < n and maze[new_x][new_y] == 0:
                new_x += dx
                new_y += dy
            # Roll back one step as the last position is a wall
            new_x -= dx
            new_y -= dy
            if (new_x, new_y) not in visited:
                queue.append((new_x, new_y))
    return False
# Example usage:
maze = [
    [0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0],
    [1, 1, 0, 1, 1],
    [0, 0, 0, 0, 0]
]
start = (4, 3)
destination = (0, 1)
print(hasPath(maze, start, destination)) 