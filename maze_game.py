import random

# Function to print the maze
def print_maze(maze):
    for row in maze:
        print(" ".join(row))

# Function to solve the maze using Depth First Search (DFS)
def solve_maze(maze, x, y):
    rows, cols = len(maze), len(maze[0])
    if x < 0 or x >= rows or y < 0 or y >= cols or maze[x][y] == "#" or maze[x][y] == "V":
        return False
    if maze[x][y] == "E":
        return True
    
    maze[x][y] = "V"
    print("\nVisiting cell:", (x, y))
    print_maze(maze)
    
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    random.shuffle(directions)
    for dx, dy in directions:
        if solve_maze(maze, x + dx, y + dy):
            return True
    
    return False

# Example usage
# Given maze
given_maze = [
    ["S", "#", ".", "#", "#"],
    [".", "#", ".", "#", "#"],
    [".", ".", ".", "#", "."],
    ["#", "#", ".", "#", "."],
    [".", ".", ".", ".", "E"]
]

print("Given Maze:")
print_maze(given_maze)

start_x, start_y = 0, 0
print("\nSolving Maze...")
if solve_maze(given_maze, start_x, start_y):
    print("\nMaze solved!")
    print_maze(given_maze)
else:
    print("\nNo solution found.")
