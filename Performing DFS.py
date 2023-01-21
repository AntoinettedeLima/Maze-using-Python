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

# Define a function to perform the DFS search
def dfs(node, visited_nodes, path):
    # Mark the current node as visited
    visited_nodes.add(node)
    # Add the current node to the path
    path.append(node)
    # Check if the current node is the goal node
    if node == goal_node:
        return True
    # Process the neighbors of the current node in increasing order
    for dx, dy in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
        x, y = np.unravel_index(node, maze.shape)
        x += dx
        y += dy
        if is_valid_move(x, y):
            neighbor = maze[x][y]
            if neighbor not in visited_nodes:
                if dfs(neighbor, visited_nodes, path):
                    return True
    # If the current node is not the goal node and all its neighbors have been processed, remove it from the path and return False
    path.pop()
    return False

# Perform the DFS search
visited_nodes = set()
path = []
time_to_find_goal = 0
found_goal = dfs(start_node, visited_nodes, path)

# Print the results of the search
if found_goal:
    time_to_find_goal = len(visited_nodes)
    print(f"Visited nodes: {visited_nodes}")
    print(f"Time to find goal: {time_to_find_goal}")
    print(f"Final path: {path}")
else:
    print("start again")
