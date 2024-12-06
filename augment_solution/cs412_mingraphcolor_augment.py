# cs412_mingraphcolor_augment.py
# Approximation solution for min graph coloring problem by Madeline Burns
# Augmented by Austin Perdue

import time

# def greedyColoring(graph):
#     # Initialize the color dictionary to -1, max amount of colors 
#     # are the amount of verticies 
#     color = {vertex: -1 for vertex in graph}
    
#     # Assign the first color to the first vertex
#     first_vertex = next(iter(graph))
#     color[first_vertex] = 0

#     # Assign colors to remaining vertices
#     for vertex in graph:
#         if color[vertex] != -1:  # Skip already colored vertex (first_vertex)
#             continue

#         # Create a set of available colors
#         available_colors = [True] * len(graph)

#         # Mark colors of adjacent vertices as unavailable
#         for neighbor in graph[vertex]:
#             if color[neighbor] != -1:
#                 available_colors[color[neighbor]] = False

#         # Find the first available color
#         for c in range(len(graph)):
#             if available_colors[c]:
#                 color[vertex] = c
#                 break

#     # Return the color assignment
#     return color

# compute lower and upper bounds
def compute_bounds(graph):
    # Upper bound: Delta + 1
    delta = max(len(neighbors) for neighbors in graph.values()) if graph else 0
    upper_bound = delta + 1

    # Lower bound:
    # Try to find a triangle for LB=3, else if there's any edge LB=2, else LB=1.
    if not graph:
        # No vertices => LB=0 or 1 if you count empty graph as 0
        return 1, upper_bound

    # Check if any edge exists
    has_edge = any(len(neighbors) > 0 for neighbors in graph.values())
    if not has_edge:
        # no edges => single vertex or isolated vertices => LB=1
        return 1, upper_bound

    # attempt to find a triangle
    # for simplicity, do a quick check
    vertices = list(graph.keys())
    found_triangle = False
    for v in vertices:
        neighbors = graph[v]
        if len(neighbors) < 2:
            continue
        #neighbor_set = set(neighbors) don't need to do this
        # check pairs of neighbors for an edge
        for i in range(len(neighbors)):
            #DEBUG: print(neighbors[i])
            for j in range(i+1, len(neighbors)):
                if neighbors[j] in graph[neighbors[i]]:
                    found_triangle = True
                    break
            if found_triangle:
                break
        if found_triangle:
            break

    if found_triangle:
        lower_bound = 3
    else:
        # no triangle, but we have at least an edge => LB=2
        lower_bound = 2

    return lower_bound, upper_bound

def dsatur_coloring(graph):
    # Initialize color assignment
    color = {v: -1 for v in graph}
    
    # Saturation and degree arrays
    saturation = {v: 0 for v in graph}
    degree = {v: len(graph[v]) for v in graph}
    
    # We'll pick the first vertex to color as the one with the highest degree (a common DSATUR start)
    current_vertex = max(graph, key=lambda v: degree[v])
    color[current_vertex] = 0
    
    # Keep track of which vertices are uncolored
    uncolored_vertices = set(graph.keys())
    uncolored_vertices.remove(current_vertex)
    
    # Update saturation for neighbors of the first chosen vertex
    for neighbor in graph[current_vertex]:
        saturation[neighbor] += 1
    
    while uncolored_vertices:
        # Select the vertex with highest saturation; tie-break by degree or vertex name
        current_vertex = max(uncolored_vertices, key=lambda v: (saturation[v], degree[v]))
        
        # Find the smallest available color not used by its neighbors
        used_colors = set()
        for neighbor in graph[current_vertex]:
            if color[neighbor] != -1:
                used_colors.add(color[neighbor])
        
        new_color = 0
        while new_color in used_colors:
            new_color += 1
        
        # Assign the new color
        color[current_vertex] = new_color
        
        # Remove from uncolored
        uncolored_vertices.remove(current_vertex)
        
        # Update saturation of its neighbors
        for neighbor in graph[current_vertex]:
            if color[neighbor] == -1:
                # The neighbor sees a new color next to it, increase saturation
                saturation[neighbor] = len(set(color[n] for n in graph[neighbor] if color[n] != -1))
    
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
    
    # Start the clock to measure the runtime of the algorithm
    start_time = time.time()

    # Perform greedy coloring
    color_assignment = dsatur_coloring(graph)
    
    # # Calculate the rutime of the algorithm
    # elapsed_time = time.time() - start_time
    # minutes = elapsed_time // 60
    # seconds = elapsed_time % 60

    # # Print the result in minutes and seconds
    # print(f"Elapsed time: {int(minutes)} minutes {round(seconds, 2)} seconds")

    # Find the number of colors used
    num_colors = max(color_assignment.values()) + 1

    # compute lower and upper bounds
    lower_bound, upper_bound = compute_bounds(graph)

    # Output
    print(num_colors)
    for vertex, color in sorted(color_assignment.items()):
        print(vertex, color)

    print(f"Elapsed time: {time.time() - start_time:.6f} seconds")
    print(f"Lower Bound: {lower_bound}")
    print(f"Upper Bound: {upper_bound}")


if __name__ == "__main__":
    main()
