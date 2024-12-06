"""
CS412 - Approx Solution for Minimum Graph Coloring
Author: Madeline Burna
Acknoledgements: 
    Used Geeks for Geeks for non-optimal help
    Used ChatGPT for help in producing test cases and .sh files
"""
def greedyColoring(graph):
    # Initialize the color dictionary to -1, max amount of colors 
    # are the amount of verticies 
    color = {vertex: -1 for vertex in graph}
    
    # Assign the first color to the first vertex
    first_vertex = next(iter(graph))
    color[first_vertex] = 0

    # Assign colors to remaining vertices
    for vertex in graph:
        if color[vertex] != -1:  # Skip already colored vertex (first_vertex)
            continue

        # Create a set of available colors
        available_colors = [True] * len(graph)

        # Mark colors of adjacent vertices as unavailable
        for neighbor in graph[vertex]:
            if color[neighbor] != -1:
                available_colors[color[neighbor]] = False

        # Find the first available color
        for c in range(len(graph)):
            if available_colors[c]:
                color[vertex] = c
                break

    # Return the color assignment
    return color


# Input processing
def process_input(edges):
    graph = {}
    for edge in edges:
        u, v = edge.split()
        if u not in graph:
            graph[u] = []
        if v not in graph:
            graph[v] = []
        graph[u].append(v)
        graph[v].append(u)
    return graph

def main():
    lines = int(input())
    edges = []
    
    for _ in range(lines):
        edges.append(input());
    
    # Process the input
    graph = process_input(edges)

    # Perform greedy coloring
    color_assignment = greedyColoring(graph)

    # Find the number of colors used
    num_colors = max(color_assignment.values()) + 1

    # Output
    print(num_colors)
    for vertex, color in sorted(color_assignment.items()):
        print(vertex, color)

if __name__ == "__main__":
    main()
