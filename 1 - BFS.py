from collections import deque, defaultdict


def add_edge(graph, u, v, directed=False):
    graph[u].append(v)
    if not directed:
        graph[v].append(u)

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    parent = {start: None}

    while queue:
        node = queue.popleft()
        if node not in visited:
            print("Visited:", node)
            visited.add(node)

            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)
                    if neighbor not in parent:
                        parent[neighbor] = node
    return parent


# def shortest_path(graph, start, target):
#     parent = bfs(graph, start)

#     if target not in parent:
#         return None 

#     path = []
#     cur = target
#     while cur is not None:
#         path.append(cur)
#         cur = parent[cur]
#     return path[::-1]


# def is_connected(graph):
#     if not graph:
#         return True
#     start = next(iter(graph))
#     parent = bfs(graph, start)
#     return len(parent) == len(graph)

if __name__ == "__main__":
    graph = defaultdict(list)


    add_edge(graph, "A", "B")
    add_edge(graph, "A", "C")
    add_edge(graph, "B", "D")
    add_edge(graph, "C", "E")
    add_edge(graph, "D", "E")
    add_edge(graph, "E", "F")
    print("\nBFS Traversal starting from A:")
    bfs(graph, "A")

    # print("\nShortest path A -> F:")
    # print(shortest_path(graph, "A", "F"))
