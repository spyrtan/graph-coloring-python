import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def plot_color_count(df):
    """Plot number of colors used by each algorithm."""
    plt.figure(figsize=(10, 6))
    sns.barplot(data=df, x="GraphType", y="Colors", hue="Algorithm")
    plt.title("Number of Colors Used by Each Algorithm")
    plt.ylabel("Number of Colors")
    plt.xlabel("Graph Type")
    plt.legend(title="Algorithm")
    plt.tight_layout()
    plt.show()

def plot_execution_time(df):
    """Plot execution time for each algorithm."""
    plt.figure(figsize=(10, 6))
    sns.barplot(data=df, x="GraphType", y="Time", hue="Algorithm")
    plt.title("Execution Time of Each Algorithm")
    plt.ylabel("Time (seconds)")
    plt.xlabel("Graph Type")
    plt.legend(title="Algorithm")
    plt.tight_layout()
    plt.show()

def main():
    # Load results from CSV file
    df = pd.read_csv("results/graph_coloring_results.csv")
    
    # Drop rows with missing values (e.g., brute force on large graphs)
    df = df.dropna()

    plot_color_count(df)
    plot_execution_time(df)

if __name__ == "__main__":
    main()
