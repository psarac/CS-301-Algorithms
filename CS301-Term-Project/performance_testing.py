import random
import networkx as nx
from timeit import default_timer as timer
import matplotlib.pyplot as plt
import numpy as np
import statistics

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

    return (path, time_elapsed)

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
    
#TESTING

time_set = []
std_set = []
#error_set = []

for node_count in range(1,51):
    
    current_time = 0
    std_of_time = []
    #error_ratio = 0
    for itr in range(100):
        
        edge_probability = random.uniform(0, 1)
        start_node = random.randint(0, node_count-1)

        G = generate_random_graph(node_count, edge_probability)
        
        # Find and mark the path using the described algorithm
        (approximation_path, time_elapsed) = mark_path(G, start_node)
        #(bruteforce_len, bruteforce_paths) = longest_path_dfs(G, start_node)
        
        current_time += time_elapsed
        std_of_time.append(time_elapsed)
        
        '''
        
        if len(approximation_path) -1 == bruteforce_len: 
            error_ratio += 1
        else: 
            error_ratio += (bruteforce_len / (len(approximation_path)-1))
        
        '''
    
    time_set.append(current_time/20) 
    std_set.append(statistics.stdev(std_of_time))
    #error_set.append(error_ratio/20)
    
    print("Finished for n =", node_count)
        
print("Mean set:",time_set)
print("Standard dev. set:",std_set)

#print(error_set)   

# Compute the corresponding input sizes
input_sizes = list(range(1, 51))

coefficients = np.polyfit(input_sizes, time_set, 3)
fit_line = np.poly1d(coefficients)

# Plotting the elapsed times
plt.plot(input_sizes, time_set, marker='o')
plt.plot(input_sizes, fit_line(input_sizes), label='Line of Best Fit')

# Set the axis labels
plt.xlabel('Input Size')
plt.ylabel('Elapsed Time (ms)')

# Set the title of the plot
plt.title('Elapsed Time vs. Input Size')

plt.legend()

# Show the plot
plt.show()
print('Function of the fitted line:')
print(fit_line)



    
        
        
        
