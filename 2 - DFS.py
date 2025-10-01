from collections import defaultdict


def add_edge(graph, u, v, directed=False):
    graph[u].append(v)
    if not directed:
        graph[v].append(u)

def dfs(graph, node, visited=None):
    if visited is None:
        visited = set()

    if node not in visited:
        print("Visited:", node)
        visited.add(node)

        for neighbor in graph[node]:
            dfs(graph, neighbor, visited)

if __name__ == "__main__":
    graph = defaultdict(list)

    add_edge(graph, "A", "B")
    add_edge(graph, "A", "C")
    add_edge(graph, "B", "D")
    add_edge(graph, "C", "E")
    add_edge(graph, "D", "E")
    add_edge(graph, "E", "F")

    print("\nDFS Traversal starting from A:")
    dfs(graph, "A")