import random
N = 8 
def is_safe(board, row, col): 
    for i in range(col):
        if board[row][i] == 1:
            return False  
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
   
    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    return True
def solve_nqueens(board, col):
    if col >= N:
      
        for row in board:
            print(row)
        return True  
    rows = list(range(N))
    random.shuffle(rows)  
    for i in rows:
        if is_safe(board, i, col):
            board[i][col] = 1
            if solve_nqueens(board, col + 1):
                return True
            board[i][col] = 0  
    return False
board = [[0]*N for _ in range(N)]
if not solve_nqueens(board, 0):
    print("No solution exists")
