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

    # Brute Force (ONLY if small graph)
    if len(graph.nodes) <= 8:
        start = time.time()
        coloring = brute_force_coloring(graph)
        duration = time.time() - start
        results["Brute Force"] = {
            "colors": len(set(coloring.values())),
            "time": duration
        }
    else:
        print(f"[INFO] Skipping Brute Force: graph too large (nodes = {len(graph.nodes)})")
        results["Brute Force"] = {
            "colors": "N/A",
            "time": "N/A"
        }

    # Backtracking (ONLY if small/medium graph)
    if len(graph.nodes) <= 12:
        start = time.time()
        coloring = backtracking_coloring(graph)
        duration = time.time() - start
        results["Backtracking"] = {
            "colors": len(set(coloring.values())),
            "time": duration
        }
    else:
        print(f"[INFO] Skipping Backtracking: graph too large (nodes = {len(graph.nodes)})")
        results["Backtracking"] = {
            "colors": "N/A",
            "time": "N/A"
        }

    return results
