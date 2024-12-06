"""
CS412 - Exact Solution for Minimum Graph Coloring
Author: Colin Gregory
Inspired by: https://www.geeksforgeeks.org/m-coloring-problem/
"""
import time

class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = {v: [] for v in vertices}  # Create an adjacency list


    def add_edge(self, u, v):
        """
        Add an edge between vertices u and v
        Args:
            u (str): The first vertex
            v (str): The second vertex
        """
        self.graph[u].append(v)
        self.graph[v].append(u)

    def is_safe(self, vertex, color_assignment, color) -> bool:
        """
        Checks if it is safe to assign the given color to the vertex
        Args:
            vertex (str): The vertex to check
            color_assignment (dict): The current color assignment
            color (int): The color to check
        Returns:
            bool: True if the color is safe, False otherwise
        """
        # Check if the color is valid for the current vertex
        for neighbor in self.graph[vertex]: # Loop over the neighbors to the current vertex
            if color_assignment.get(neighbor) == color: # If its color is the same as the color of the current vertex, return false
                return False
        return True # WOOHOO! The color is safe

    def graph_color_util(self, color_assignment, colors, index) -> bool:
        """
        Recursive utility function to assign colors to vertices
        Args:
            color_assignment (dict): The current color assignment
            colors (list): The list of available colors
            index (int): The index of the vertex to process
        Returns:
            bool: True if a valid coloring is found, False otherwise

        Note: test case 12_clique.txt and 216_clique.txt take more than 20 minutes to run
        """
        # Base case
        if index == len(self.vertices):
            return True

        vertex = self.vertices[index]
        for color in colors: # Loop over the colors
            if self.is_safe(vertex, color_assignment, color): # Using the is_safe function, check if the color is safe
                color_assignment[vertex] = color # If it is, then assign the color to the vertex
                if self.graph_color_util(color_assignment, colors, index + 1): # Recursively call the function for the next vertex (the index + 1)
                    return True
                # Backtrack
                del color_assignment[vertex] # If the color is not safe, backtrack and remove the color assignment
        return False

    def find_min_coloring(self) -> tuple:
        """
        Find the minimum number of colors needed to color the graph
        Returns:
            tuple: The number of colors and the color assignment
        """
        # Increment the number of colors until a valid coloring is found
        for num_colors in range(1, len(self.vertices) + 1):
            color_assignment = {}
            colors = list(range(num_colors)) #Create a list 1 - num_colors
            if self.graph_color_util(color_assignment, colors, 0):
                return num_colors, color_assignment

        return None  # Should not happen for a connected graph, but if some vertices are not connected, this will be reached i think


def main():
    # Read input
    num_edges = int(input())
    edges = [input().split() for _ in range(num_edges)]
    
    # Get all vertices
    vertices = set()
    for u, v in edges:
        vertices.add(u)
        vertices.add(v)
    vertices = sorted(vertices)  # Ensure deterministic ordering

    # Create the graph
    graph = Graph(vertices)
    for u, v in edges:
        graph.add_edge(u, v)

    start_time = time.time()
    # Find the minimum coloring
    num_colors, color_assignment = graph.find_min_coloring()

    # Print output in the specified format
    print(num_colors)
    # for vertex in vertices:
    #     print(f"{vertex} {color_assignment[vertex]}")
    
    print(f"Elapsed time: {time.time() - start_time:.6f} seconds")

if __name__ == "__main__":
    main()
