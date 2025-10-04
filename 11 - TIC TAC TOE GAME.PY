board = [" "] * 9
players = ["X", "O"]

def show():
    for i in range(0, 9, 3):
        print(board[i], "|", board[i+1], "|", board[i+2])
        if i < 6: print("--+---+--")

def win(p):
    combos = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
    return any(all(board[i]==p for i in c) for c in combos)

turn = 0
while " " in board:
    show()
    p = players[turn%2]
    move = int(input(f"Player {p}, choose (0-8): "))
    if board[move]==" ":
        board[move]=p
        if win(p):
            show(); print(f"🎉 Player {p} wins!"); break
        turn+=1
    else: print("Taken, try again!")
else:
    show(); print("It's a draw!")
