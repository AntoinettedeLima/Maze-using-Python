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

# Define a function to check if a node is a valid move
def is_valid_move(x, y):
    # Check if the node is within the bounds of the maze
    if x < 0 or x >= maze.shape[0] or y < 0 or y >= maze.shape[1]:
        return False
    # Check if the node is a barrier node
    if maze[x][y] in barrier_nodes:
        return False
    return True

# Define a function to calculate the heuristic cost for a given node
def heuristic_cost(node):
    # Get the (x, y) coordinates of the node
    x, y = np.unravel_index(node, maze.shape)
    # Get the (x, y) coordinates of the goal node
    goal_x, goal_y = np.unravel_index(goal_node, maze.shape)
    # Calculate the Chebyshev Distance using the formula given above
    cost = max(abs(x - goal_x), abs(y - goal_y))
    return cost

# Define a function to perform the A* search
def a_star(start, goal):
    # Initialize the open and closed sets
    open_set = set([start])
    closed_set = set()
    # Initialize the g-scores and f-scores for the starting node
    g_scores = {start: 0}
    f_scores = {start: g_scores[start] + heuristic_cost(start)}
    # Initialize the came_from dictionary
    came_from = {}
    # While
