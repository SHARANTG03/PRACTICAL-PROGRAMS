from collections import deque


def get_moves(state, X, Y):
    a, b = state
    moves = []

    
    moves.append((X, b))
    
    moves.append((a, Y))
    
    moves.append((0, b))
    
    moves.append((a, 0))
   
    pour = min(a, Y - b)
    moves.append((a - pour, b + pour))
    
    pour = min(b, X - a)
    moves.append((a + pour, b - pour))

    return moves


def bfs(X, Y, Z):
    start = (0, 0)
    queue = deque([[start]])
    visited = set([start])

    while queue:
        path = queue.popleft()
        state = path[-1]

       
        if state[0] == Z or state[1] == Z:
            return path

        for move in get_moves(state, X, Y):
            if move not in visited:
                visited.add(move)
                queue.append(path + [move])
    return None



if __name__ == "__main__":
    X, Y, Z = 4, 3, 2  
    print("BFS Solution (Shortest Path):")
    solution = bfs(X, Y, Z)
    print(solution)
