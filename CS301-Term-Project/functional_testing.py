import random
import networkx as nx
from timeit import default_timer as timer

def generate_random_graph(n, p_edge):
    G = nx.Graph()
    for i in range(n):
        G.add_node(i)
    for i in range(n):
        for j in range(i+1, n):
            p = random.random()
            if p <= p_edge:
                G.add_edge(i, j)
    return G


def mark_path(graph, start_node):
    
    start = timer()
    # Step 0: Input checks
    if type(graph) != type(nx.Graph()):
        print('Non-graph Input')
        return []
    if graph.number_of_nodes() == 0:
        print('Empty Graph')
        return []
    if type(start_node) != int:
        print('Non-integer Start Node')
        return []
    if start_node < 0:
        print('Negative Start Node')
        return []
    if start_node > graph.number_of_nodes()-1 :
        print('Start Node Too Large')
        return []
    
    # Step 1: Initialize variables
    path = []

    # Step 2: Mark vertices until no further marking is possible
    current_vertex = start_node
    print('Initialized variables and set current_vertex to start_node')
    while current_vertex is not None:
        # Mark the current vertex
        path.append(current_vertex)
        print('Marked current_vertex and appended it to the path')

        # Find unmarked neighbors of the current vertex
        unmarked_neighbors = [neighbor for neighbor in graph[current_vertex] if neighbor not in path]
        
        if unmarked_neighbors:
            print('There are unmarked neighbors')
            # Step 2: Pick the vertex with the smallest integer value among unmarked neighbors
            current_vertex = min(unmarked_neighbors, key=int)
        else:
            print('There are no unmarked neighbors')
            # No unmarked neighbors, terminate the loop
            current_vertex = None
            
    end = timer()
    time_elapsed = round(1000*(end - start), 6)
    print('Returning the path')
    return (path, time_elapsed)



print()
#TESTING

# TEST CASE 1
#G = nx.Graph() # Empty Graph
#start_node = 0 # Otherwise Valid Start Node
#approximation_path = mark_path(G, start_node)

# TEST CASE 2
#edge_probability = random.uniform(0, 1)
#node_count = random.randint(1, 15)
#start_node = 'Test' # String Start Node
#G = generate_random_graph(node_count, edge_probability)
#approximation_path = mark_path(G, start_node)

# TEST CASE 3
#edge_probability = random.uniform(0, 1)
#node_count = random.randint(1, 15)
#start_node = 1.537 # Float Start Node
#G = generate_random_graph(node_count, edge_probability)
#approximation_path = mark_path(G, start_node)

# TEST CASE 4
#edge_probability = random.uniform(0, 1)
#node_count = random.randint(1, 15)
#start_node = -2 # Negative Start Node
#G = generate_random_graph(node_count, edge_probability)
#approximation_path = mark_path(G, start_node)

# TEST CASE 5
#edge_probability = random.uniform(0, 1)
#node_count = random.randint(1, 15)
#start_node = node_count+1 # Start Node Larger Than Node Count
#G = generate_random_graph(node_count, edge_probability)
#approximation_path = mark_path(G, start_node)

# TEST CASE 6
#edge_probability = random.uniform(0, 1)
#node_count = 1 # Graph With 1 Node
#start_node = random.randint(0, node_count-1)  
#G = generate_random_graph(node_count, edge_probability)
#approximation_path = mark_path(G, start_node)

# TEST CASE 7
#edge_probability = random.uniform(0, 1)
#node_count = random.randint(1, 15)
#start_node = random.randint(0, node_count-1)  
#G = 3 # Non-graph Input
#approximation_path = mark_path(G, start_node)

