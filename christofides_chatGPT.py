# import numpy as np
# import networkx as nx

# def christofides(cities):
#     # Find the minimum spanning tree of the graph
#     mst = minimum_spanning_tree(cities)
    
#     # Identify the nodes (cities) that have odd degree in the minimum spanning tree
#     odd_degree_nodes = [node for node in range(len(cities)) if mst.degree(node) % 2 == 1]
    
#     # Find a minimum weight perfect matching on the set of odd degree nodes
#     matching = minimum_weight_matching(cities, odd_degree_nodes)
    
#     # Add the edges from the minimum weight perfect matching to the minimum spanning tree to create a multigraph
#     multigraph = mst.copy()
#     for u, v in matching:
#         multigraph.add_edge(u, v, weight=cities[u][v])
        
#     # Find an Eulerian circuit in the multigraph
#     circuit = eulerian_circuit(multigraph)
    
#     # Remove the edges that are included in the Eulerian circuit from the multigraph to obtain a Hamiltonian circuit
#     tour = []
#     for u, v in circuit:
#         if multigraph.has_edge(u, v):
#             tour.append((u, v))
#             multigraph.remove_edge(u, v)
#     tour.append((u, v))
    
#     return tour

# def minimum_spanning_tree(cities):
#     # Create a graph from the distance matrix
#     graph = nx.Graph()
#     for i in range(len(cities)):
#         for j in range(len(cities)):
#             if i != j:
#                 graph.add_edge(i, j, weight=cities[i][j])
    
#     # Use Kruskal's algorithm to find the minimum spanning tree of the graph
#     mst = nx.minimum_spanning_tree(graph)
    
#     return mst

# def minimum_weight_matching(cities, nodes):
#     # Create a bipartite graph from the distance matrix and the set of odd degree nodes
#     graph = nx.Graph()
#     for i in nodes:
#         for j in nodes:
#             if i != j:
#                 graph.add_edge(i, j, weight=cities[i][j])
    
#     # Use the Blossom algorithm to find a minimum weight perfect matching on the set of odd degree nodes
#     matching = nx.algorithms.matching.max_weight_matching(graph, True)
    
#     return matching

# def eulerian_circuit(graph):
#     # Initialize an empty circuit
#     circuit = []
    
#     # Choose an arbitrary starting vertex
#     start = next(iter(graph))
#     current = start
    
#     # Keep track of the visited vertices
#     visited = set()
    
#     # Iterate until all vertices have been visited
#     while len(visited) < graph.number_of_nodes():
#         # Add the current vertex to the circuit
#         circuit.append((current, start))
#         visited.add(current)
        
#         # Find the first unvisited neighbor of the current vertex
#         for neighbor in graph[current]:
#             if neighbor not in visited:
#                 # Move to the neighbor and continue the search
#                 current = neighbor
#                 break
#         else:
#             # If there are no unvisited neighbors, move back to the starting vertex
#             current = start
    
#     return circuit

# # import numpy as np
# # import networkx as nx

# # def christofides(cities):
# #     # Find the minimum spanning tree of the graph
# #     mst = minimum_spanning_tree(cities)
    
# #     # Identify the nodes (cities) that have odd degree in the minimum spanning tree
# #     odd_degree_nodes = [node for node in range(len(cities)) if mst.degree(node) % 2 == 1]
    
# #     # Find a minimum weight perfect matching on the set of odd degree nodes
# #     matching = minimum_weight_matching(cities, odd_degree_nodes)
    
# #     # Create a new graph from the minimum weight perfect matching
# #     matching_graph = nx.Graph()
# #     for u, v in matching:
# #         matching_graph.add_edge(u, v, weight=cities[u][v])
    
# #     # Add the matching graph to the minimum spanning tree to create a multigraph
# #     # Add the edges from the minimum weight perfect matching to the minimum spanning tree to create a multigraph
# #     multigraph = nx.disjoint_union(mst, matching_graph, rename=('mst-', 'matching-'))

    
# #     # Find an Eulerian circuit in the multigraph using Hierholzer's algorithm
# #     circuit = hierholzer(multigraph)
    
# #     # Remove the edges that are included in the Eulerian circuit from the multigraph to obtain a Hamiltonian circuit
# #     tour = []
# #     for u, v in circuit:
# #         if multigraph.has_edge(u, v):
# #             tour.append((u, v))
# #             multigraph.remove_edge(u, v)
# #     tour.append((u, v))
    
# #     return tour


# # def minimum_spanning_tree(cities):
# #     # Create a graph from the distance matrix
# #     graph = nx.Graph()
# #     for i in range(len(cities)):
# #         for j in range(len(cities)):
# #             if i != j:
# #                 graph.add_edge(i, j, weight=cities[i][j])
    
# #     # Use Kruskal's algorithm to find the minimum spanning tree of the graph
# #     mst = nx.minimum_spanning_tree(graph)
    
# #     return mst

# # def minimum_weight_matching(cities, nodes):
# #     # Create a bipartite graph from the distance matrix and the set of odd degree nodes
# #     graph = nx.Graph()
# #     for i in nodes:
# #         for j in nodes:
# #             if i != j:
# #                 graph.add_edge(i, j, weight=cities[i][j])
    
# #     # Use the Blossom algorithm to find a minimum weight perfect matching on the set of odd degree nodes
# #     matching = nx.algorithms.matching.max_weight_matching(graph, True)
    
# #     # Convert the matching from a set to a list of tuples
# #     matching = [(u, v) for u, v in matching]
    
# #     return matching


# # def hierholzer(graph):
# #     # Initialize an empty circuit
# #     circuit = []
    
# #     # Choose an arbitrary starting vertex
# #     start = next(iter(graph))
# #     current = start
    
# #     # Keep track of the visited vertices
# #     visited = set()
    
# #     # Iterate until all vertices have been visited
# #     while len(visited) < graph.number_of_nodes():
# #         # Add the current vertex to the circuit
# #         circuit.append((current, start))
# #         visited.add(current)
        
# #         # Find the first unvisited neighbor of the current vertex
# #         for neighbor in graph[current]:
# #             if neighbor not in visited:
# #                 # Move to the neighbor and continue the search
# #                 current = neighbor
# #                 break
# #         else:
# #             # If there are no unvisited neighbors, move back to the starting vertex
# #             current = start
    
# #     return circuit


import numpy as np
import networkx as nx

def christofides(cities):
    # Find the minimum spanning tree of the graph
    mst = minimum_spanning_tree(cities)
    print(mst)
    
    # Identify the nodes (cities) that have odd degree in the minimum spanning tree
    odd_degree_nodes = [node for node in range(len(cities)) if mst.degree(node) % 2 == 1]
    print(odd_degree_nodes)
    
    # Find a minimum weight perfect matching on the set of odd degree nodes
    matching = minimum_weight_matching(cities, odd_degree_nodes)
    print(matching)
    
    # Add the edges from the minimum weight perfect matching to the minimum spanning tree to create a multigraph
    multigraph = mst.copy()
    for u, v in matching:
        multigraph.add_edge(u, v, weight=cities[u][v])
    print(multigraph)
        
    # Find an Eulerian circuit in the multigraph using Hierholzer's algorithm
    circuit = hierholzer(multigraph)
    print(circuit)
    
    # Remove the edges that are included in the Eulerian circuit from the multigraph to obtain a Hamiltonian circuit
    tour = []
    for u, v in circuit:
        if multigraph.has_edge(u, v):
            tour.append((u, v))
            multigraph.remove_edge(u, v)
    tour.append((u, v))
    
    return tour

def minimum_spanning_tree(cities):
    # Create a graph from the distance matrix
    graph = nx.Graph()
    for i in range(len(cities)):
        for j in range(len(cities)):
            if i != j:
                graph.add_edge(i, j, weight=cities[i][j])
    
    # Use Kruskal's algorithm to find the minimum spanning tree of the graph
    mst = nx.minimum_spanning_tree(graph)
    
    return mst

def minimum_weight_matching(cities, nodes):
    # Create a bipartite graph from the distance matrix and the set of odd degree nodes
    graph = nx.Graph()
    for i in nodes:
        for j in nodes:
            if i != j:
                graph.add_edge(i, j, weight=cities[i][j])
    
    # Use the Blossom algorithm to find a minimum weight perfect matching on the set of odd degree nodes
    matching = nx.algorithms.matching.max_weight_matching(graph, True)
    
    # Convert the matching from a set to a list of tuples
    matching = [(u, v) for u, v in matching]
    
    return matching

def hierholzer(graph):
    # Initialize an empty circuit
    circuit = []
    
    # Choose an arbitrary starting vertex
    start = next(iter(graph))
    current = start
    
    # Keep track of the visited vertices
    visited = set()
    
    # Iterate until all vertices have been visited
    while len(visited) < graph.number_of_nodes():
        # Add the current vertex to the circuit
        circuit.append((current, start))
        visited.add(current)
        
        # Find the first unvisited neighbor of the current vertex
        for neighbor in graph[current]:
            if neighbor not in visited:
                # Move to the neighbor and continue the search
                current = neighbor
                break
        else:
            # If there are no unvisited neighbors, move back to the starting vertex
            current = start
    
    return circuit




# Create a distance matrix for a set of cities
cities = np.array([
    [0, 1, 2, 3],
    [1, 0, 4, 5],
    [2, 4, 0, 6],
    [3, 5, 6, 0]
])

tour = christofides(cities)
# Find the final tour using the Christofides algorithm

print(tour)