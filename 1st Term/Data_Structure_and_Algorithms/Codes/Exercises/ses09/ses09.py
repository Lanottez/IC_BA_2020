# This command imports data structures from ses09_graphs.py
# It will only work if the Spyder working directory is the one where the file is located
# Change the working directory using the folder icon in the top right corner
import ses09_graphs as gs


def lecture_graph():
    """
    Returns the lecture directed graph example adjacency list as a dictionary
    
    Complete the dictionary below
    
    Examples:
    >>> adj_list = lecture_graph()
    >>> adj_list['d']['e']
    2
    >>> 'd' in adj_list['e']
    False
    >>> [adj_list[n][m] for n in 'abcde' for m in 'abcde' if m in adj_list[n]]
    [1, 5, 2, 5, 2, 6, 2]
    >>> [len(adj_list[n]) for n in 'abcde']
    [2, 2, 2, 1, 0]
    """
    distances = {
        'a': {},
        'b': {'c': 2, 'd': 5},
        'c': {},
        'd': {},
        'e': {}
    }
    return distances


def dijkstra(graph, start):
    """ 
    Shortest distances using Dijkstra's algorithm 
    
    Polynomial-time implementation. 
    
    Assumes that there is a path from start node to all other nodes in graph.
    
    Parameters:
        graph: a Graph (or Digraph) 
        start: starting node for the algorithm
    Returns: 
        dists: dictionary containing shortest distances to all nodes
        prev_nodes: dictionary containing the previous node from which each node was explored
                None for the starting node
    
    Examples:
    >>> graph = gs.Digraph(lecture_graph())
    >>> dists, prev_nodes = dijkstra(graph, 'a')
    >>> [dists['b'], dists['e'], dists['c'], dists['d']]
    [1, 7, 3, 5]
    >>> [prev_nodes['a'], prev_nodes['e'], prev_nodes['c'], prev_nodes['d']]
    [None, 'd', 'b', 'c']
    """
    # DON'T CHANGE ANYTHING ABOVE
    # YOUR CODE BELOW
    
    # Initialize algorithm
    
    # Visited nodes X initially empty  
    X = set()
    X.add(start)
    
    # Previous nodes
    prev_nodes = ...
    
    # Shortest distances to all nodes from s
    A = dict() 
    for node in graph.get_nodes(): 
        A[node] = float('Inf') # initialize to "infinity"
        
    A[start] = 0 # distance zero to itself

    # Main loop
    # Loop while we haven't visited all nodes
    while len(X) < len(graph.get_nodes()): 
         
        # Store mininimum edge and distance when looping
        min_edge = [] # list [src, dest, weight]
        min_dist = float('inf')
        
        # Loop through all edges starting in X and not ending in X
        # Find minimum Dijksta score
        for src in X:
            for dest, weight in graph.children_of(src): # edges starting from src
                if dest not in X: # edge not ending in X
                    # Update minimum-Dijkstra-score edge if find one
                    if A[src] + weight < min_dist: 
                        min_edge = [src, dest, weight] 
                        min_dist = A[src] + weight 
        # Update A[min_e_dest] = A[min_e_source] + A[min_e_weight]        
        A[min_edge[1]] = A[min_edge[0]] + min_edge[2]
        
        # Add destination node from min edge to visited nodes
        X.add(min_edge[1])  
    
    return A


def print_path(prev_nodes, v):
    """ 
    Based on dictionary prev_nodes containing links to previous nodes, 
    prints out path from starting node to v.
    """
    
    path_list = []
    while v is not None:
        path_list.append(v)
        v = prev_nodes[v]
    
    path_list = reversed(path_list)    
    path = ' -> '.join(path_list)
    print(path)




