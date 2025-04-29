import os
import csv
import matplotlib.pyplot as plt
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

def save_results_to_csv(results, filename="data/graph_coloring_results.csv", metadata=None):
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
                colors = data["colors"] if data["colors"] != "N/A" else "N/A"
                time = f"{data['time']:.6f}" if isinstance(data["time"], (int, float)) else "N/A"

                writer.writerow([graph_type, size, algorithm, colors, time])
                print(f"[DEBUG] Saved: {graph_type}, {size}, {algorithm}, {colors}, {time}")

        print("[INFO] Results saved successfully ✅")

    except Exception as e:
        print(f"[ERROR] Failed to save results: {e}")

def visualize_colorings(graph):
    print("\n[INFO] Showing colorized graphs for each algorithm...")

    draw_graph(graph, greedy_largest_first(graph), "Greedy LF Coloring")
    draw_graph(graph, greedy_smallest_last(graph), "Greedy SL Coloring")
    draw_graph(graph, greedy_saturation_largest_first(graph), "Greedy SLF Coloring")

    if len(graph.nodes) <= 16:
        draw_graph(graph, brute_force_coloring(graph), "Brute Force Coloring")

    if len(graph.nodes) <= 30:
        draw_graph(graph, backtracking_coloring(graph), "Backtracking Coloring")

def plot_runtime_comparison(results):
    algorithms = []
    times = []

    for algo, res in results.items():
        if isinstance(res["time"], (int, float)):
            algorithms.append(algo)
            times.append(res["time"])

    plt.figure(figsize=(10, 6))
    plt.bar(algorithms, times, color="skyblue")
    plt.title("Porównanie czasu działania algorytmów")
    plt.xlabel("Algorytm")
    plt.ylabel("Czas [sekundy]")
    plt.xticks(rotation=45)
    plt.tight_layout()

    plot_filename = "results/runtime_comparison.png"
    plt.savefig(plot_filename)
    print(f"[INFO] Wykres zapisany do: {plot_filename}")

    plt.show()

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
            colors = res['colors'] if res['colors'] != "N/A" else "N/A"
            time = f"{res['time']:.6f}" if isinstance(res['time'], (int, float)) else "N/A"
            print(f"{algo:15} | Colors: {colors} | Time: {time} sec")

        if save:
            metadata = {
                "GraphType": graph_type,
                "Size": parameters.get("num_nodes") or (parameters.get("width") * parameters.get("height"))
            }
            save_results_to_csv(results, metadata=metadata)

        if i == 0:
            visualize_colorings(graph)
            plot_runtime_comparison(results)

if __name__ == "__main__":
    main()
