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
    while current_vertex is not None:
        # Mark the current vertex
        path.append(current_vertex)

        # Find unmarked neighbors of the current vertex
        unmarked_neighbors = [neighbor for neighbor in graph[current_vertex] if neighbor not in path]
        
        if unmarked_neighbors:
            # Step 2: Pick the vertex with the smallest integer value among unmarked neighbors
            current_vertex = min(unmarked_neighbors, key=int)
        else:
            # No unmarked neighbors, terminate the loop
            current_vertex = None
            
    end = timer()
    time_elapsed = round(1000*(end - start), 6)
    return path

def DFS(G,v,seen=None,path=None):
    
    paths = []
    if seen is None: seen = []
    if path is None: 
        path = [v]
        paths.append(path)

    seen.append(v)

    
    for t in G[v]:
        if t not in seen:
            t_path = path + [t]
            paths.append(tuple(t_path))
            paths.extend(DFS(G, t, seen[:], t_path))
    return paths

def longest_path_dfs(G, start_node):
    
    all_paths = DFS(G, start_node)
    max_len   = max(len(p) for p in all_paths)
    max_paths = [p for p in all_paths if len(p) == max_len]
    
    return (max_len-1, max_paths)


# INITIAL TESTING

edge_probability = random.uniform(0, 1)
node_count = random.randint(1, 10)
start_node = random.randint(0, node_count-1)
G = generate_random_graph(node_count, edge_probability)

print("Edge Probability:", edge_probability)
print("Node Count:", node_count)

# Find and mark the path using the described algorithm
approximation_path = mark_path(G, start_node)
(bruteforce_len, bruteforce_paths) = longest_path_dfs(G, start_node)

# Output the path
print()
print("Approximation Path Length:", len(approximation_path)-1)
print("Approximation Path:", approximation_path)
print()
print("Brute Force Path Length:", bruteforce_len)
print("Same Path Length:", "Yes" if len(approximation_path)-1 == bruteforce_len else "No")
