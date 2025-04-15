import time
import networkx as nx

from src.graph_generator import get_graph
from src.greedy_algorithms import (
    greedy_largest_first,
    greedy_smallest_last,
    greedy_saturation_largest_first
)
from src.brute_force import brute_force_coloring
from src.backtracking import backtracking_coloring


def run_experiment(graph: nx.Graph) -> dict:
    """
    Runs all graph coloring algorithms on a given graph and records the results.

    Returns a dictionary with the number of colors used and computation time for each algorithm.
    """
    results = {}

    # Greedy - Largest First
    start = time.time()
    coloring = greedy_largest_first(graph)
    duration = time.time() - start
    results["Greedy LF"] = {
        "colors": len(set(coloring.values())),
        "time": duration
    }

    # Greedy - Smallest Last
    start = time.time()
    coloring = greedy_smallest_last(graph)
    duration = time.time() - start
    results["Greedy SL"] = {
        "colors": len(set(coloring.values())),
        "time": duration
    }

    # Greedy - Saturation Largest First (DSATUR)
    start = time.time()
    coloring = greedy_saturation_largest_first(graph)
    duration = time.time() - start
    results["Greedy SLF"] = {
        "colors": len(set(coloring.values())),
        "time": duration
    }

    # Brute Force - only for small graphs
    if len(graph.nodes) <= 8:
        start = time.time()
        coloring = brute_force_coloring(graph)
        duration = time.time() - start
        results["Brute Force"] = {
            "colors": len(set(coloring.values())),
            "time": duration
        }
    else:
        results["Brute Force"] = {"colors": None, "time": None}

    # Backtracking - only for small/medium graphs
    if len(graph.nodes) <= 12:
        start = time.time()
        coloring = backtracking_coloring(graph)
        duration = time.time() - start
        results["Backtracking"] = {
            "colors": len(set(coloring.values())),
            "time": duration
        }
    else:
        results["Backtracking"] = {"colors": None, "time": None}

    return results


if __name__ == "__main__":
    # Example run
    g = get_graph("random", num_nodes=6, edge_prob=0.4)
    summary = run_experiment(g)
    for algo, stats in summary.items():
        print(f"{algo:15} | Colors: {stats['colors']} | Time: {stats['time']:.6f} sec")
