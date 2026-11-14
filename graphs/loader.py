from .undirected_graph import UndirectedGraph
from .directed_graph import DirectedGraph


def load_graph_from_file(file_path, directed=False):
    """Read a text file with lines 'source,target,weight' and build a graph."""
    graph = DirectedGraph() if directed else UndirectedGraph()
    with open(file_path, encoding="utf-8") as file:
        for line_number, line in enumerate(file, start=1):
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            parts = [p.strip() for p in line.split(",")]
            if parts[0].lower() == "source":  # optional header
                continue
            if len(parts) == 1:  # isolated vertex
                graph.add_vertex(parts[0])
                continue
            if len(parts) not in (2, 3):
                raise ValueError(f"Invalid line {line_number}: {line}")
            weight = float(parts[2]) if len(parts) == 3 else 1.0
            graph.add_edge(parts[0], parts[1], weight)
    return graph
