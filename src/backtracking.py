import networkx as nx

def backtracking_coloring(graph: nx.Graph) -> dict:
    """
    Backtracking algorithm to color the graph using the minimum number of colors.
    """
    nodes = list(graph.nodes())
    coloring = {}

    def is_safe(node, color):
        return all(coloring.get(neigh) != color for neigh in graph.neighbors(node))

    def backtrack(index, max_color):
        if index == len(nodes):
            return True

        node = nodes[index]
        for color in range(max_color):
            if is_safe(node, color):
                coloring[node] = color
                if backtrack(index + 1, max_color):
                    return True
                del coloring[node]

        return False

    for num_colors in range(1, len(nodes) + 1):
        coloring.clear()
        if backtrack(0, num_colors):
            return coloring

    return {}
