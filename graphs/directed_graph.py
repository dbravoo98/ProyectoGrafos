class DirectedGraph:
    """Directed graph represented with an adjacency matrix.

    vertex_index maps each vertex to a row/column; matrix[i][j] holds the
    weight of the edge i -> j, or None when there is no edge.
    """

    def __init__(self):
        self.vertex_index = {}
        self.vertices = []
        self.matrix = []

    def add_vertex(self, vertex):
        if vertex in self.vertex_index:
            return
        self.vertex_index[vertex] = len(self.vertices)
        self.vertices.append(vertex)
        for row in self.matrix:
            row.append(None)
        self.matrix.append([None] * len(self.vertices))

    def add_edge(self, source, target, weight=1.0):
        self.add_vertex(source)
        self.add_vertex(target)
        self.matrix[self.vertex_index[source]][self.vertex_index[target]] = weight

    def get_vertices(self):
        return list(self.vertices)

    def get_neighbors(self, vertex):
        """Successors of vertex (outgoing edges)."""
        i = self.vertex_index[vertex]
        return [self.vertices[j] for j, w in enumerate(self.matrix[i]) if w is not None]

    def get_edges(self):
        return [(self.vertices[i], self.vertices[j], w)
                for i, row in enumerate(self.matrix)
                for j, w in enumerate(row) if w is not None]

    def vertex_count(self):
        return len(self.vertices)

    def edge_count(self):
        return len(self.get_edges())

    def is_directed(self):
        return True

    def __str__(self):
        header = "    " + " ".join(f"{str(v):>5}" for v in self.vertices)
        rows = [f"{str(v):>3} " + " ".join(f"{'-' if w is None else w:>5}" for w in row)
                for v, row in zip(self.vertices, self.matrix)]
        return "\n".join([header] + rows)
