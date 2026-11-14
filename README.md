# Proyecto Matemáticas Discretas II

Universidad del Valle. 
David Bravo Ospina - 2371758
Implementación de grafos en Python con entorno gestionado por uv.

## Estructura
- `graphs/undirected_graph.py`: grafo no dirigido con **lista de adyacencia**.
- `graphs/directed_graph.py`: grafo dirigido con **matriz de adyacencia**.
- `graphs/loader.py`: `load_graph_from_file(path, directed=False)` lee líneas `source,target,weight`.
- `graphs/properties.py`: `is_connected`, `has_cycles`, `is_tree`, `is_forest` `<funcion>: <resultado>`
- `data/`: archivos de ejemplo.

## Cómo correrlo
```bash
uv run main.py                              # corre todos los ejemplos
uv run main.py data/tree.txt                # un archivo, no dirigido
uv run main.py data/directed.txt --directed # un archivo, dirigido
```

## Por qué estas implementaciones
- **Lista de adyacencia (no dirigido):** usa memoria proporcional a vértices + aristas y permite recorrer los vecinos de un vértice rápido, que es justo lo que necesitan DFS/BFS para conexidad y ciclos. Cada arista se guarda en ambos sentidos.
- **Matriz de adyacencia (dirigido):** permite saber en O(1) si existe la arista u→v y deja ver claramente la asimetría de un grafo dirigido. Su costo es O(V²) de memoria, aceptable para grafos pequeños.

## Decisiones
- Conexidad: DFS desde un vértice; en dirigidos se evalúa conexidad débil (grafo subyacente).
- Ciclos: en no dirigidos, DFS guardando el padre; en dirigidos, DFS con colores (blanco/gris/negro).
- Árbol: conexo y sin ciclos. Bosque: sin ciclos.

## Sobre el proyecto
Lo más retador fue detectar ciclos distinguiendo el caso dirigido del no dirigido; la representación con lista facilitó los recorridos y la matriz hizo sencillo verificar aristas.
