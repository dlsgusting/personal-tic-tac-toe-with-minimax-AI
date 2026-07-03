playing = True
current = 1

board = ["?","?","?","?","?","?","?","?","?"]

wins = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [1,4,7],
    [2,5,8],
    [3,6,8],
    [1,5,9],
    [3,5,7]
]

def check_win():
    global playing
    for win in wins:
        pos1 = win[0]
        pos2 = win[1]
        pos3 = win[2]

        if board[pos1-1] == board[pos2-1] == board[pos3-1] and board[pos1-1] != "?":
            if board[pos1] == "O":
                print("P1 wins!")
                playing = False
            elif board[pos1] == "X":
                print("P2 wins!")
                playing = False

def display_board():
    for i, item in enumerate(board, start=1):
        print(item, end="   ")
        if i % 3 == 0:
            print("\n")

def place():
    valid = [1,2,3,4,5,6,7,8,9]
    while True:
        try:
            print("Choose a position 1-9")
            pos = int(input())

            if pos not in valid:
                Print("Not a valid position, choose again")
            elif board[pos-1] != "?":
                print("Position already taken, choose again")
            else:
                break
        except ValueError:
            print("Not a valid position, choose again")
    
    return pos

def turn():
    global current
    if current == 1:
        print("Player 1 turn")
    else:
        print("Player 2 turn")
    pos = place()

    if current == 1:
        board[pos-1] = "O"
    else:
        board[pos-1] = "X"

    current = -current

while playing:
    print()
    display_board()
    check_win()
    turn()

