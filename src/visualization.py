import matplotlib.pyplot as plt
import networkx as nx
from matplotlib.colors import TABLEAU_COLORS
import os

def draw_graph(graph, coloring, title="Graph Coloring", save=True, show=True):
    # Generate layout for node positions
    pos = nx.spring_layout(graph, seed=42)

    # Assign colors
    unique_colors = list(set(coloring.values()))
    color_palette = list(TABLEAU_COLORS.values())
    node_colors = []

    for node in graph.nodes:
        color_idx = coloring.get(node, -1)
        if color_idx == -1:
            node_colors.append("gray")
        else:
            node_colors.append(color_palette[color_idx % len(color_palette)])

    # Plot the graph
    plt.figure(figsize=(8, 6))
    nx.draw(
        graph,
        pos,
        with_labels=True,
        node_color=node_colors,
        edge_color="gray",
        node_size=600,
        font_size=10
    )
    plt.title(title)

    # Save to file
    if save:
        os.makedirs("results/plots", exist_ok=True)
        safe_title = title.lower().replace(" ", "_")
        filepath = f"results/plots/{safe_title}.png"
        plt.savefig(filepath)
        print(f"[INFO] Graph saved to: {filepath}")

    # Show graph
    if show:
        plt.show()

    plt.clf()
