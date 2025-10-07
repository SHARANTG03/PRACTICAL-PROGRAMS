import random
from collections import deque

def solve_8_puzzle_random(start):
    start = tuple(sum(start, []))
    goal = (0,1,2,3,4,5,6,7,8)
    moves = {0:[1,3],1:[0,2,4],2:[1,5],3:[0,4,6],4:[1,3,5,7],5:[2,4,8],6:[3,7],7:[4,6,8],8:[5,7]}
    queue = deque([(start, start.index(0), 0)])
    visited = {start}

    while queue:
        state, zero, depth = queue.popleft()
        if state == goal:
            return random.randint(1, 20)
        for move in moves[zero]:
            new_state = list(state)
            new_state[zero], new_state[move] = new_state[move], new_state[zero]
            new_state = tuple(new_state)
            if new_state not in visited:
                visited.add(new_state)
                queue.append((new_state, move, depth + 1))
    return random.randint(1, 20)


puzzle = [[3,1,2],[4,7,5],[6,8,0]]
print(solve_8_puzzle_random(puzzle))
