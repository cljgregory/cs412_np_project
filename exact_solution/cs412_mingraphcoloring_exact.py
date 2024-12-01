import time
from itertools import product

def main():
    """
    Main function for reading input and creating the graph as well as timing the algorithm.
    """
    # Read number of edges
    num_edges = int(input())
    
    # Build the graph from edge list
    graph = {}
    edges = []
    for _ in range(num_edges):
        u, v = input().split()
        edges.append((u, v))
        if u not in graph:
            graph[u] = []
        if v not in graph:
            graph[v] = []
        graph[u].append(v)
        graph[v].append(u)
    
    # Find all vertices
    vertices = list(graph.keys())

    start_time = time.time()
    # Find the minimum coloring
    min_coloring = find_min_coloring(graph, vertices)
    
    # Print the min coloring, the colors for vertices, and the time taken
    num_colors = len(set(min_coloring.values()))
    print(num_colors)
    for vertex, color in min_coloring.items():
        print(f"{vertex} {color}")
    
    elapsed_time = time.time() - start_time
    minutes = elapsed_time // 60
    seconds = elapsed_time % 60

    # Print the result in minutes and seconds
    print(f"Elapsed time: {int(minutes)} minutes {round(seconds, 2)} seconds")

# Function to find the minimum coloring
def find_min_coloring(graph, vertices):
    """
    This function finds the minimum coloring of a graph by finding all possible colorings and checking if they are valid.
    Uses the product function from itertools to generate all possible colorings as discussed in class.
    Args:
        graph: A dictionary representing the graph.
        vertices: A list of vertices in the graph.
    Returns:
        A dictionary mapping vertices to colors.

    """
    num_vertices = len(vertices)
    colors = list(range(num_vertices))  # Colors from 0 to num_vertices - 1
    
    # Try all possible colorings
    for coloring in product(colors, repeat=num_vertices):
        assignment = dict(zip(vertices, coloring))
        if is_valid_coloring(graph, assignment):
            return assignment  # Return valid coloring
    
    return {}


def is_valid_coloring(graph, coloring):
    """
    Function for checking if a graph coloring is valid which should run in polynomial time.
    Args:
        graph: A dictionary representing the graph.
        coloring: A dictionary mapping vertices to colors.
    Returns:
        True if the coloring is valid, False otherwise.

    Note: Help for this function was found in a YouTube video by NeuralNine
    Link: https://www.youtube.com/watch?v=AyrrZ4PCyws
    """
    for vertex, neighbors in graph.items():
        for neighbor in neighbors:
            if coloring[vertex] == coloring[neighbor]:
                return False
    return True

if __name__ == "__main__":
    main()





