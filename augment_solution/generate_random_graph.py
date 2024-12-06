import random
import string
# AUSTIN PERDUE
# HELPER METHOD TO GENERATE RANDOM GRAPHS FOR TESTING

def generate_random_graph(num_vertices=15, num_edges=200):
    # Generate random vertex names
    # Use random letters or letter combinations to avoid alphabetical ordering benefits
    vertices = ["".join(random.choices(string.ascii_uppercase + string.ascii_lowercase, k=3)) 
                for _ in range(num_vertices)]
    
    # Use a set to avoid duplicate edges
    edges_set = set()
    
    # Randomly add edges between distinct vertices
    while len(edges_set) < num_edges:
        u = random.choice(vertices)
        v = random.choice(vertices)
        if u != v:
            edge = tuple(sorted([u, v]))
            edges_set.add(edge)
    
    edges = list(edges_set)
    # Shuffle edges to randomize insertion order
    random.shuffle(edges)
    
    # Print out in the required format
    print(len(edges))
    for (u, v) in edges:
        print(u, v)

if __name__ == "__main__":
    generate_random_graph()
