def hasPath(maze, start, destination):
    def dfs(x, y):
        # Check if the current position is the destination
        if [x, y] == destination:
            return True
        
        # Mark the current position as visited
        maze[x][y] = 2
        
        # Define possible moves: Up, Down, Left, Right
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        for dx, dy in directions:
            # Keep rolling in the current direction until hitting a wall or border
            newX, newY = x, y
            while 0 <= newX+dx < len(maze) and 0 <= newY+dy < len(maze[0]) and maze[newX+dx][newY+dy] != 1:
                newX += dx
                newY += dy
            
            # If the new position is not visited, explore it
            if maze[newX][newY] == 0 and dfs(newX, newY):
                return True
        
        return False

    # Call the DFS function from the starting point
    return dfs(start[0], start[1])

# Test data
maze = [
    [0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0],
    [1, 1, 0, 1, 1],
    [0, 0, 0, 0, 0]
]
start = [4, 3]
destination = [0, 1]

print(hasPath(maze, start, destination)) 
