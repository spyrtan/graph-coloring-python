# graph-coloring-python
A Python-based project focused on solving the graph coloring problem using discrete optimization techniques.
![image](https://github.com/user-attachments/assets/6047bf8c-fd65-4e70-bebf-afb44d19abf6)

Graph Coloring Python Project
This repository contains a modular implementation of various graph coloring algorithms.

Project Structure
css
Kopiuj
Edytuj
graph_coloring_python/
│
├── src/
│   ├── graph_generator.py
│   ├── greedy_algorithms.py
│   ├── brute_force.py
│   ├── backtracking.py
│   ├── experiment.py
│   └── plot_results.py
│
├── data/
│
├── results/
│
└── main.py
Description
src/: Contains the main source code files:

graph_generator.py: Generates graphs for experiments.

greedy_algorithms.py: Implements greedy-based coloring algorithms.

brute_force.py: Provides a brute-force solution for graph coloring.

backtracking.py: Implements graph coloring using the backtracking approach.

experiment.py: Organizes and runs different graph coloring experiments.

plot_results.py: Plots and visualizes results of the experiments.

data/: Stores generated and colored graphs.

results/: Stores output results such as performance plots and graphs after experiments.

main.py:
The main entry point that manages the workflow:

Generates graphs.

Applies graph coloring algorithms.

Saves generated and colored graphs into the data/ directory.

Saves experiment results and plots into the results/ directory.

Usage
To run the project:

bash
Kopiuj
Edytuj
python main.py
