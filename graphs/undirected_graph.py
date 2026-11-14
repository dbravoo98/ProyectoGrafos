class UndirectedGraph:
    """Undirected graph represented with an adjacency list.
    adjacency[u] = {v: weight, ...}; every edge is stored in both directions.
    """

    def __init__(self):
        self.adjacency = {}

    def add_vertex(self, vertex):
        if vertex not in self.adjacency:
            self.adjacency[vertex] = {}

    def add_edge(self, source, target, weight=1.0):
        self.add_vertex(source)
        self.add_vertex(target)
        self.adjacency[source][target] = weight
        self.adjacency[target][source] = weight

    def get_vertices(self):
        return list(self.adjacency.keys())

    def get_neighbors(self, vertex):
        return list(self.adjacency.get(vertex, {}).keys())

    def get_edges(self):
        edges, seen = [], set()
        for u, neighbors in self.adjacency.items():
            for v, w in neighbors.items():
                key = frozenset((u, v))
                if key not in seen:
                    seen.add(key)
                    edges.append((u, v, w))
        return edges

    def vertex_count(self):
        return len(self.adjacency)

    def edge_count(self):
        return len(self.get_edges())

    def is_directed(self):
        return False

    def __str__(self):
        lines = [f"{u} -> {neighbors}" for u, neighbors in self.adjacency.items()]
        return "\n".join(lines)
