"""Graph properties. Each function returns its result and prints
'<function_name>: <result>'. Directed graphs use their underlying
undirected graph for connectivity/tree/forest, and real directed cycles
for has_cycles."""


def _undirected_neighbors(graph):
    neighbors = {v: set() for v in graph.get_vertices()}
    for u, v, _ in graph.get_edges():
        neighbors[u].add(v)
        neighbors[v].add(u)
    return neighbors


def _check_connected(graph):
    vertices = graph.get_vertices()
    if not vertices:
        return True
    neighbors = _undirected_neighbors(graph)
    visited, stack = {vertices[0]}, [vertices[0]]
    while stack:
        for nxt in neighbors[stack.pop()]:
            if nxt not in visited:
                visited.add(nxt)
                stack.append(nxt)
    return len(visited) == len(vertices)


def _check_undirected_cycles(graph):
    """DFS keeping the parent; reaching a visited vertex that is not the parent means a cycle.
    A self-loop also counts as a cycle."""
    if graph.is_directed():
        edges = graph.get_edges()
        # underlying undirected: anti-parallel edges u->v, v->u form a 2-cycle there too
        pairs = set()
        for u, v, _ in edges:
            if u == v or frozenset((u, v)) in pairs:
                return True
            pairs.add(frozenset((u, v)))
    neighbors = {v: graph.get_neighbors(v) for v in graph.get_vertices()} \
        if not graph.is_directed() else _undirected_neighbors(graph)
    visited = set()
    for start in graph.get_vertices():
        if start in visited:
            continue
        visited.add(start)
        stack = [(start, None)]
        while stack:
            current, parent = stack.pop()
            for nxt in neighbors[current]:
                if nxt == current:
                    return True
                if nxt not in visited:
                    visited.add(nxt)
                    stack.append((nxt, current))
                elif nxt != parent:
                    return True
    return False


def _check_directed_cycles(graph):
    #DFS with colors: finding a GRAY vertex means a cycle.
    WHITE, GRAY, BLACK = 0, 1, 2
    color = {v: WHITE for v in graph.get_vertices()}
    for start in graph.get_vertices():
        if color[start] != WHITE:
            continue
        color[start] = GRAY
        stack = [(start, iter(graph.get_neighbors(start)))]
        while stack:
            vertex, children = stack[-1]
            child = next(children, None)
            if child is None:
                color[vertex] = BLACK
                stack.pop()
            elif color[child] == GRAY:
                return True
            elif color[child] == WHITE:
                color[child] = GRAY
                stack.append((child, iter(graph.get_neighbors(child))))
    return False


def is_connected(graph):
    result = _check_connected(graph)
    print(f"is_connected: {result}")
    return result


def has_cycles(graph):
    result = _check_directed_cycles(graph) if graph.is_directed() else _check_undirected_cycles(graph)
    print(f"has_cycles: {result}")
    return result


def is_tree(graph):
    #A tree is a connected graph without cycles.
    result = _check_connected(graph) and not _check_undirected_cycles(graph)
    print(f"is_tree: {result}")
    return result


def is_forest(graph):
    #A forest is a graph without cycles.
    result = not _check_undirected_cycles(graph)
    print(f"is_forest: {result}")
    return result
