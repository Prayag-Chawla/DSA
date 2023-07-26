def is_valid_move(maze, x, y, n):
    # Check if the move is within the bounds of the maze and the cell is not blocked
    return 0 <= x < n and 0 <= y < n and maze[x][y] == 1

def solve_maze_helper(maze, x, y, n, solution):
    # Base case: If the rat reaches the destination (bottom-right corner)
    if x == n - 1 and y == n - 1:
        solution[x][y] = 1
        return True


    if is_valid_move(maze, x, y, n):
     
        solution[x][y] = 1

        if solve_maze_helper(maze, x, y + 1, n, solution):
            return True

        if solve_maze_helper(maze, x + 1, y, n, solution):
            return True

        
        solution[x][y] = 0
        return False

    return False

def solve_maze(maze):
    n = len(maze)
    
  
    solution = [[0 for _ in range(n)] for _ in range(n)]


    if solve_maze_helper(maze, 0, 0, n, solution):
        print("Path exists. Solution:")
        for row in solution:
            print(row)
    else:
        print("No path exists.")


maze = [
    [1, 0, 0, 0],
    [1, 1, 0, 1],
    [0, 1, 0, 0],
    [1, 1, 1, 1]
]

solve_maze(maze)
