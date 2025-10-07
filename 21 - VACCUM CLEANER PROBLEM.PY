from collections import deque

def vacuum(start, goal):
    visited = set()
    queue = deque([(start, [])])
    while queue:
        state, path = queue.popleft()
        if state == goal:
            return path
        if state not in visited:
            visited.add(state)
            for i in range(2):
                
                if state[i] == 'D':
                    next_state = tuple('C' if j == i else state[j] for j in range(2))
                    queue.append((next_state, path + [next_state]))
    return None

start = ('D', 'D')
goal = ('C', 'C')

print(vacuum(start, goal))
