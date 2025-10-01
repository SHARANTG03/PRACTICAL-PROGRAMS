
game_tree = [
    [3, 5, 2],       
    [9, 1, 2],       
    [0, -1, -2]      
]


def max_value(node):
    if isinstance(node, int):  
        return node
    max_val = float('-inf')
    for child in node:
        val = min_value(child)  
        max_val = max(max_val, val)
    return max_val


def min_value(node):
    if isinstance(node, int): 
        return node
    min_val = float('inf')
    for child in node:
        val = max_value(child)  
        min_val = min(min_val, val)
    return min_val


best_value = max_value(game_tree)
print("Best value for MAX:", best_value)
