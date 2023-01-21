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

# Set the goal node using its (x, y) coordinates
goal_node = maze[4][3]

# Define a function to calculate the heuristic cost for a given node
def heuristic_cost(node):
    # Get the (x, y) coordinates of the node
    x, y = np.unravel_index(node, maze.shape)
    # Get the (x, y) coordinates of the goal node
    goal_x, goal_y = np.unravel_index(goal_node, maze.shape)
    # Calculate the Chebyshev Distance using the formula given above
    cost = max(abs(x - goal_x), abs(y - goal_y))
    return cost

# Calculate the heuristic cost for the node 8 in the maze
node = maze[2][1]  # Node 8 in this example
cost = heuristic_cost(node)
print(f"Heuristic cost for node {node}: {cost}")
