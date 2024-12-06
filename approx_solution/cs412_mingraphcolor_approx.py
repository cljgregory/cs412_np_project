import time
# input a simple undirected graph G with verticies V as well as a list of colors

# def greedyColoring(graph):
#     colors = [-1 for _ in range(len(graph[1]))]

    # function greedyColoring(graph): 
    # // Step 1: Initialize the color array 
    # let color[] = array of size graph.numberOfVertices initialized to -1 
 

    # // Step 2: Assign the first color to the first vertex 
    # color[0] = 0 
 
    # // Step 3: Assign colors to remaining vertices 
    # for vertex in range(1, graph.numberOfVertices): 
    #     // Step 3.1: Create a set of available colors 
    #     let availableColors = array of size graph.numberOfVertices initialized to true 
 
    #     // Step 3.2: Mark colors of adjacent vertices as unavailable 
    #     for neighbor in graph.adjacencyList[vertex]: 
    #         if color[neighbor] != -1: 
    #             availableColors[color[neighbor]] = false 
 
    #     // Step 3.3: Find the first available color 
    #     for c in range(0, graph.numberOfVertices): 
    #         if availableColors[c]: 
    #             color[vertex] = c 
    #             break 
 
    # // Step 4: Return the color assignment 
    # return color
    

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
    
    # Start the clock to measure the runtime of the algorithm
    start_time = time.time()

    # Perform greedy coloring
    color_assignment = greedyColoring(graph)
    
    # # Calculate the rutime of the algorithm
    # elapsed_time = time.time() - start_time
    # minutes = elapsed_time // 60
    # seconds = elapsed_time % 60

    # # Print the result in minutes and seconds
    # print(f"Elapsed time: {int(minutes)} minutes {round(seconds, 2)} seconds")

    # Find the number of colors used
    num_colors = max(color_assignment.values()) + 1

    # Output
    print(num_colors)
    for vertex, color in sorted(color_assignment.items()):
        print(vertex, color)

    print(f"Elapsed time: {time.time() - start_time:.6f} seconds")

if __name__ == "__main__":
    main()
