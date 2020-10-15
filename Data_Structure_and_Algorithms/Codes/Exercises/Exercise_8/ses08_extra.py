
from ses08_data_structures import Graph, Digraph, Queue, QueueNode

def create_dfs_graph():
    """
    Initializes a test graph for DFS
    """
    g = Graph()
    g.add_edge('John', 'Helena')
    g.add_edge('John', 'Chris')
    g.add_edge('Helena', 'Paul')
    g.add_edge('Chris', 'Paul')
    g.add_edge('Chris', 'Vicki')
    g.add_edge('Jared', 'Vicki')
    g.add_edge('Jared', 'Donald')
    g.add_edge('Jared', 'Paul')
    return g


def dfs(graph, start):
    """
    Depth first search on graph from node start
    
    Parameters: 
        graph (Digraph/Graph), 
        start: starting node in the graph
    
    Returns:
        prev_nodes: dictionary:
            key: node, value: node where this node was reached from
        pop_order: dictionary:
            key: node, value: the order in which this node was removed from the list
         
    Example use:
    >>> lec_graph = create_dfs_graph()
    >>> dfs_paths, pop_order = dfs(lec_graph, 'John')
    >>> abs(pop_order['Chris'] - pop_order['Helena']) > 1
    True
    """
    # DON'T CHANGE ANYTHING ABOVE
    # YOUR CODE BELOW
    