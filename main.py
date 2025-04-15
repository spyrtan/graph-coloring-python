import os
import csv
from src.graph_generator import get_graph
from src.experiment import run_experiment
from src.greedy_algorithms import (
    greedy_largest_first,
    greedy_smallest_last,
    greedy_saturation_largest_first
)
from src.brute_force import brute_force_coloring
from src.backtracking import backtracking_coloring
from src.visualization import draw_graph


def prompt_graph_type():
    print("Select graph type:")
    print("1 - Random graph")
    print("2 - Grid graph")
    print("3 - Complete graph")
    print("4 - Tree graph")
    choice = input("Enter choice (1-4): ")
    types = {"1": "random", "2": "grid", "3": "complete", "4": "tree"}
    return types.get(choice, "random")


def get_graph_parameters(graph_type):
    if graph_type == "grid":
        width = int(input("Enter grid width: "))
        height = int(input("Enter grid height: "))
        return {"width": width, "height": height}
    else:
        num_nodes = int(input("Enter number of nodes: "))
        params = {"num_nodes": num_nodes}
        if graph_type == "random":
            edge_prob = float(input("Enter edge probability (e.g., 0.3): "))
            params["edge_prob"] = edge_prob
        return params


def save_results_to_csv(results, filename="results/graph_coloring_results.csv", metadata=None):
    os.makedirs("results", exist_ok=True)
    file_exists = os.path.isfile(filename)

    print(f"\n[INFO] Saving results to: {filename}")

    try:
        with open(filename, mode="a", newline="") as f:
            writer = csv.writer(f)
            if not file_exists:
                writer.writerow(["GraphType", "Size", "Algorithm", "Colors", "Time"])

            for algorithm, data in results.items():
                size = metadata.get("Size", "N/A")
                graph_type = metadata.get("GraphType", "unknown")
                writer.writerow([graph_type, size, algorithm, data["colors"], data["time"]])
                print(f"[DEBUG] Saved: {graph_type}, {size}, {algorithm}, {data['colors']}, {data['time']:.6f}")

        print("[INFO] Results saved successfully ✅")

    except Exception as e:
        print(f"[ERROR] Failed to save results: {e}")


def visualize_colorings(graph):
    print("\n[INFO] Showing colorized graphs for each algorithm...")

    draw_graph(graph, greedy_largest_first(graph), "Greedy LF Coloring")
    draw_graph(graph, greedy_smallest_last(graph), "Greedy SL Coloring")
    draw_graph(graph, greedy_saturation_largest_first(graph), "Greedy SLF Coloring")

    if len(graph.nodes) <= 8:
        draw_graph(graph, brute_force_coloring(graph), "Brute Force Coloring")

    if len(graph.nodes) <= 12:
        draw_graph(graph, backtracking_coloring(graph), "Backtracking Coloring")


def main():
    print("Graph Coloring Experiment Runner")

    graph_type = prompt_graph_type()
    parameters = get_graph_parameters(graph_type)
    num_runs = int(input("Enter number of runs (e.g., 3): "))
    save = input("Save results to CSV file? (y/n): ").strip().lower() == "y"

    for i in range(num_runs):
        print(f"\nRunning experiment {i + 1} of {num_runs}...")
        graph = get_graph(graph_type, **parameters)
        results = run_experiment(graph)

        for algo, res in results.items():
            print(f"{algo:15} | Colors: {res['colors']} | Time: {res['time']:.6f} sec")

        if save:
            metadata = {
                "GraphType": graph_type,
                "Size": parameters.get("num_nodes") or (parameters.get("width") * parameters.get("height"))
            }
            save_results_to_csv(results, metadata=metadata)

        # Only visualize on first run to avoid spamming windows
        if i == 0:
            visualize_colorings(graph)


if __name__ == "__main__":
    main()
