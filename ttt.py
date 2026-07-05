running = True
current = -1
board = ["?","?","?","?","?","?","?","?","?"]

wins = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [1,4,7],
    [2,5,8],
    [3,6,9],
    [1,5,9],
    [3,5,7]
]

def check_win(board):
    for win in wins:
        pos1 = win[0]
        pos2 = win[1]
        pos3 = win[2]

        if board[pos1-1] == board[pos2-1] == board[pos3-1] and board[pos1-1] != "?":
            if board[pos1-1] == "O":
                return "player"
            elif board[pos1-1] == "X":
                return "ai"

    if "?" not in board:
        return 0

    return None

def minimax(board, current_turn):
    result = check_win(board)

    if result == "ai":
        return 1
    elif result == "player":
        return -1
    elif result == 0:
        return 0

    if current_turn == 1:
        best_score = -999

        for pos in range(len(board)):
            if board[pos] == "?":
                board[pos] = "X"
                score = minimax(board, -1)
                board[pos] = "?"
                best_score = max(score, best_score)

        return best_score

    else:
        best_score = 999

        for pos in range(len(board)):
            if board[pos] == "?":
                board[pos] = "O"
                score = minimax(board, 1)
                board[pos] = "?"
                best_score = min(score, best_score)

        return best_score


def ai_turn(board):
    best_score = -999
    best_move = None

    for pos in range(len(board)):
        if board[pos] == "?":
            board[pos] = "X"
            score = minimax(board, -1)
            board[pos] = "?"
            
            if score > best_score:
                best_score = score
                best_move = pos

    if best_move is not None:
        board[best_move] = "X"

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
                print("Not a valid position, choose again")
            elif board[pos-1] != "?":
                print("Position already taken, choose again")
            else:
                break
        except ValueError:
            print("Not a valid position, choose again")
    
    return pos

def player_turn():
    pos = place()
    board[pos -1] = "O"

# def turn():
#     global current
#     if current == 1:
#         print("Player 1 turn")
#     else:
#         print("Player 2 turn")
#     pos = place()

#     if current == 1:
#         board[pos-1] = "O"
#     else:
#         board[pos-1] = "X"

#     current = -current

while running:
    print()
    display_board()
    result = check_win(board)

    if result == "ai":
        print("AI wins")
        running = False
        break
    elif result == "player":
        print("Player wins")
        running = False
        break
    elif result == 0:
        print("Draw")
        running = False
        break

    player_turn()
    ai_turn(board)