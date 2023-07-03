import random
import networkx as nx

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



def longest_path_brute_force(G, s, t, k):
    stack = [(s, [s])]
    while stack:
        (vertex, path) = stack.pop()
        if vertex == t and len(path)-1 >= k:
            print("Path:", path)
            return True
        else: 
            for neighbor in G[vertex]:
                if neighbor not in path:
                    stack.append((neighbor, path + [neighbor]))
    return False



edge_probability = random.uniform(0, 1)
node_count = random.randint(1, 20)
min_edges = random.randint(0, node_count-1)
start_node = random.randint(0, node_count-1)
end_node = random.randint(0, node_count-1)

G = generate_random_graph(node_count, edge_probability)


print("Result:", longest_path_brute_force(G, start_node, end_node, min_edges))
print("Edge Probability:", edge_probability)
print("Node Count:", node_count)
print("Minimum number of edges (k):", min_edges)
print("Start Node:", start_node)
print("End Node:", end_node)
