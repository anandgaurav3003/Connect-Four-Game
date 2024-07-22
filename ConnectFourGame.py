import random

print("Welcome to Connect Four")
print("-----------------------")

possibleLetters = ["A", "B", "C", "D", "E", "F", "G"]
gameBoard = [["" for _ in range(7)] for _ in range(6)]
rows = 6
cols = 7

def printGameBoard():
    print("\n     A    B    C    D    E    F    G  ", end="")
    for x in range(rows):
        print("\n   +----+----+----+----+----+----+----+")
        print(x, " |", end="")
        for y in range(cols):
            if gameBoard[x][y] == "🔵" or gameBoard[x][y] == "🔴":
                print("", gameBoard[x][y], end=" |")
            else:
                print(" ", gameBoard[x][y], end="  |")
    print("\n   +----+----+----+----+----+----+----+")

def modifyTurn(col, turn):
    for row in range(rows - 1, -1, -1):
        if gameBoard[row][col] == "":
            gameBoard[row][col] = turn
            return row, col

def is_valid_location(col):
    return gameBoard[0][col] == ""

def check_winner(board, piece):
    # Check horizontal locations for win
    for c in range(cols - 3):
        for r in range(rows):
            if board[r][c] == piece and board[r][c + 1] == piece and board[r][c + 2] == piece and board[r][c + 3] == piece:
                return True

    # Check vertical locations for win
    for c in range(cols):
        for r in range(rows - 3):
            if board[r][c] == piece and board[r + 1][c] == piece and board[r + 2][c] == piece and board[r + 3][c] == piece:
                return True

    # Check positively sloped diagonals
    for c in range(cols - 3):
        for r in range(rows - 3):
            if board[r][c] == piece and board[r + 1][c + 1] == piece and board[r + 2][c + 2] == piece and board[r + 3][c + 3] == piece:
                return True

    # Check negatively sloped diagonals
    for c in range(cols - 3):
        for r in range(3, rows):
            if board[r][c] == piece and board[r - 1][c + 1] == piece and board[r - 2][c + 2] == piece and board[r - 3][c + 3] == piece:
                return True

    return False

def get_column_index(letter):
    return possibleLetters.index(letter.upper())

turnCounter = 0
game_over = False

while not game_over:
    printGameBoard()
    
    if turnCounter % 2 == 0:
        player = "🔵"
        col = input("Player 1 (🔵), choose a column (A-G): ").upper()
    else:
        player = "🔴"
        col = input("Player 2 (🔴), choose a column (A-G): ").upper()
    
    if col in possibleLetters:
        col_index = get_column_index(col)
        
        if is_valid_location(col_index):
            row, col_index = modifyTurn(col_index, player)
            
            if check_winner(gameBoard, player):
                printGameBoard()
                print(f"Player {'1 (🔵)' if player == '🔵' else '2 (🔴)'} wins!")
                game_over = True
        else:
            print("Column is full! Choose another column.")
    else:
        print("Invalid column! Choose a column between A-G.")
    
    turnCounter += 1
    
    if turnCounter == rows * cols:
        print("The game is a draw!")
        game_over = True

print("Game Over!")
