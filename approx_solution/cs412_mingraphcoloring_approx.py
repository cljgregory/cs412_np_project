# input a simple undirected graph G with verticies V as well as a list of colors

# for i = 1 to n do
# set c[i] = to the first color in L[i]

# for each j with i < j and (vi, vj) ! E(G) do
# Set Lj := Lj/ci
# Return eah vertex, the color it was assigned, and total the number of colors used



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