import networkx as nx
from collections import defaultdict

def greedy_largest_first(graph: nx.Graph) -> dict:
    """
    Colors the graph using the Largest First greedy algorithm.
    Vertices are colored in descending order of degree.
    """
    nodes = sorted(graph.nodes(), key=lambda x: graph.degree[x], reverse=True)
    return greedy_coloring(graph, nodes)

def greedy_smallest_last(graph: nx.Graph) -> dict:
    """
    Colors the graph using the Smallest Last greedy algorithm.
    Nodes are removed one by one by smallest degree and colored in reverse order.
    """
    temp_graph = graph.copy()
    ordering = []

    while temp_graph.nodes:
        node = min(temp_graph.nodes, key=lambda x: temp_graph.degree[x])
        ordering.append(node)
        temp_graph.remove_node(node)

    ordering.reverse()
    return greedy_coloring(graph, ordering)

def greedy_saturation_largest_first(graph: nx.Graph) -> dict:
    """
    Colors the graph using the Saturation Largest First (DSATUR) algorithm.
    Nodes with the highest saturation degree are chosen first.
    """
    color_assignment = {}
    saturation = defaultdict(int)
    degrees = dict(graph.degree())

    while len(color_assignment) < len(graph.nodes):
        uncolored = [n for n in graph.nodes if n not in color_assignment]

        # Get node with max saturation, then max degree
        next_node = max(uncolored, key=lambda n: (saturation[n], degrees[n]))

        used_colors = {color_assignment[neigh] for neigh in graph.neighbors(next_node) if neigh in color_assignment}
        color = 0
        while color in used_colors:
            color += 1
        color_assignment[next_node] = color

        # Update saturation
        for neigh in graph.neighbors(next_node):
            if neigh not in color_assignment:
                saturation[neigh] = len({color_assignment[n] for n in graph.neighbors(neigh) if n in color_assignment})

    return color_assignment

def greedy_coloring(graph: nx.Graph, node_order: list) -> dict:
    """
    Helper function to apply greedy coloring based on given node order.
    """
    color_assignment = {}
    for node in node_order:
        neighbor_colors = {color_assignment[neighbor] for neighbor in graph.neighbors(node) if neighbor in color_assignment}
        color = 0
        while color in neighbor_colors:
            color += 1
        color_assignment[node] = color
    return color_assignment
