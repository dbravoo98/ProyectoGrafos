import sys
from graphs import load_graph_from_file, is_connected, has_cycles, is_tree, is_forest


def analyze(file_path, directed):
    kind = "directed" if directed else "undirected"
    graph = load_graph_from_file(file_path, directed=directed)
    print(f"\n=== {file_path} ({kind}) ===")
    print(graph)
    is_connected(graph)
    has_cycles(graph)
    is_tree(graph)
    is_forest(graph)


def main():
    if len(sys.argv) > 1:
        analyze(sys.argv[1], directed="--directed" in sys.argv)
        return
    for path in ["data/tree.txt", "data/cycle.txt", "data/forest.txt"]:
        analyze(path, directed=False)
    analyze("data/directed.txt", directed=True)


if __name__ == "__main__":
    main()
