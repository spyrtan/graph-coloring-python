import networkx as nx
import random

def generate_random_graph(num_nodes: int, edge_prob: float) -> nx.Graph:
    """Generates a random Erdos-Renyi graph."""
    return nx.erdos_renyi_graph(num_nodes, edge_prob)

def generate_grid_graph(width: int, height: int) -> nx.Graph:
    """Generates a 2D grid graph (mesh)."""
    return nx.grid_2d_graph(width, height)

def generate_complete_graph(num_nodes: int) -> nx.Graph:
    """Generates a complete graph (clique)."""
    return nx.complete_graph(num_nodes)

def generate_tree_graph(num_nodes: int) -> nx.Graph:
    """Generates a random tree with a specified number of nodes."""
    return nx.balanced_tree(5, num_nodes - 1)

def get_graph(graph_type: str, **kwargs) -> nx.Graph:
    """
    Wrapper function to get a graph based on user-specified type and parameters.
    
    Parameters:
        graph_type (str): 'random', 'grid', 'complete', 'tree'
        kwargs: Parameters for the specific graph type

    Returns:
        nx.Graph: Generated graph
    """
    if graph_type == "random":
        return generate_random_graph(kwargs.get("num_nodes", 10), kwargs.get("edge_prob", 0.3))
    elif graph_type == "grid":
        return generate_grid_graph(kwargs.get("width", 4), kwargs.get("height", 4))
    elif graph_type == "complete":
        return generate_complete_graph(kwargs.get("num_nodes", 10))
    elif graph_type == "tree":
        return generate_tree_graph(kwargs.get("num_nodes", 10))
    else:
        raise ValueError(f"Unknown graph type: {graph_type}")
