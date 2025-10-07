def is_valid(graph, colors, node, c):
    for adj in range(len(graph)):
        if graph[node][adj] == 1 and colors[adj] == c:
            return False
    return True
def backtrack(graph, colors, node=0):
    if node == len(graph):
        return True
    for c in range(1, colors + 1):
        if is_valid(graph, color_assignment, node, c):
            color_assignment[node] = c
            if backtrack(graph, colors, node + 1):
                return True
            color_assignment[node] = 0
    return False
graph = [
    [0, 1, 1, 1],  
    [1, 0, 1, 0],  
    [1, 1, 0, 1],  
    [1, 0, 1, 0]   
]

color_assignment = [0] * len(graph)
num_colors = 3
if backtrack(graph, num_colors):
    print("Coloring solution:", color_assignment)
else:
    print("No solution with", num_colors, "colors.")
