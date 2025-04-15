import networkx as nx
import itertools

def is_valid_coloring(graph: nx.Graph, coloring: dict) -> bool:
    """Checks whether the given coloring is valid (no adjacent nodes share the same color)."""
    for u, v in graph.edges():
        if coloring.get(u) == coloring.get(v):
            return False
    return True

def brute_force_coloring(graph: nx.Graph, max_colors: int = None) -> dict:
    """
    Brute-force graph coloring. Tries all color combinations up to max_colors.
    Only feasible for very small graphs!
    """
    nodes = list(graph.nodes())
    n = len(nodes)
    max_colors = max_colors or n

    for num_colors in range(1, max_colors + 1):
        for colors in itertools.product(range(num_colors), repeat=n):
            coloring = dict(zip(nodes, colors))
            if is_valid_coloring(graph, coloring):
                return coloring

    return {}  # No valid coloring found