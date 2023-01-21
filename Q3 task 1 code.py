import numpy as np

# Define the maze as a 2D array of integers
maze = np.array([
    [1, 2, 3, 4, 5, 6],
    [7, 8, 9, 10, 11, 12],
    [13, 14, 15, 16, 17, 18],
    [19, 20, 21, 22, 23, 24],
    [25, 26, 27, 28, 29, 30],
    [31, 32, 33, 34, 35, 36]
])

# Set the starting node and goal node using their (x, y) coordinates
start_node = maze[2][1]
goal_node = maze[4][3]

# Set the barrier nodes using their (x, y) coordinates
barrier_nodes = [
    maze[0][0],
    maze[1][2],
    maze[2][1],
    maze[3][3]
]
