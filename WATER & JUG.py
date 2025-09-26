from collections import deque

# Generate all possible moves
def get_moves(state, X, Y):
    a, b = state
    moves = []

    # Fill Jug1
    moves.append((X, b))
    # Fill Jug2
    moves.append((a, Y))
    # Empty Jug1
    moves.append((0, b))
    # Empty Jug2
    moves.append((a, 0))
    # Pour Jug1 -> Jug2
    pour = min(a, Y - b)
    moves.append((a - pour, b + pour))
    # Pour Jug2 -> Jug1
    pour = min(b, X - a)
    moves.append((a + pour, b - pour))

    return moves

# BFS for Water Jug Problem
def bfs(X, Y, Z):
    start = (0, 0)
    queue = deque([[start]])
    visited = set([start])

    while queue:
        path = queue.popleft()
        state = path[-1]

        # Goal check
        if state[0] == Z or state[1] == Z:
            return path

        for move in get_moves(state, X, Y):
            if move not in visited:
                visited.add(move)
                queue.append(path + [move])
    return None


# ---------------- DRIVER CODE ----------------
if __name__ == "__main__":
    X, Y, Z = 4, 3, 2   # Jug1=4L, Jug2=3L, Target=2L
    print("BFS Solution (Shortest Path):")
    solution = bfs(X, Y, Z)
    print(solution)
