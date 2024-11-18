# IDEAS FOR EXACT SOLUTION
# Find every possible coloring of the graph regardless of if it is correct or not
# Bounds for coloring will be 1 to n where n is the number of vertices
# Sift through all possible colorings and check if they are valid using 2 loops?
# If valid, check if it is the minimum coloring
# If it is, store it and continue checking for other colorings
# If it is not, continue checking for other colorings
# Return the minimum coloring found


# Input
# -1st line, number of vertices (N)
# -The next N lines will first assume the vertex and then the vertices that it is connected to
# Output
# -The minimum number of colors needed to color the graph
# -The time it took to find the minimum coloring
# -Extra: PRINT COLORS?

# Example
# Input
# 5
# 1 2 3 4
# 2 1 3 4
# 3 1 2 4
# 4 1 2 3 5
# 5 4
# Output
# 4
# Found solution in X.XX seconds
import time
from itertools import product

def main():
    num_vert = int(input("Input num vertices: "))

    graph = {}
    for num in range(num_vert):
        # Read input and convert to integers
        graph[num] = list(map(int, input().split()))
    
    start_time = time.time()
    # Find the minimum coloring
    min_coloring = find_min_coloring(graph, num_vert)
    print(min_coloring, "minimum colors")

    elapsed_time = time.time() - start_time
    rounded_time = round(elapsed_time, 4)
    print(f"{rounded_time} seconds")  # Output rounded time

# Generator to yield colorings and check them one at a time
def find_min_coloring(graph, num_vert):
    # List of colors (1 to num_vert)
    colors = [i for i in range(1, num_vert + 1)]
    
    # Iterate over all possible colorings (using product to generate colorings)
    for coloring in product(colors, repeat=num_vert):
        if all(check_vertex_coloring(graph, vertex, coloring) for vertex in graph):
            return len(set(coloring))  # Return the number of unique colors used
    
    return 0

# Check if the coloring is valid for a specific vertex
def check_vertex_coloring(graph, vertex, coloring):
    for neighbor in graph[vertex]:
        if coloring[vertex] == coloring[neighbor]:
            return False
    return True

main()




