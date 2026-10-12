# Tic-Tac-Toe Game State Validator

# Write a program that analyzes a 3×3 Tic-Tac-Toe board and determines the current state of the game.

# The board contains three possible values:

# X — Player X's move
# O — Player O's move
# - — Empty cell

# The program should:

# Take the 3×3 board as input.
# Count the total number of X and O moves.
# Check whether X has won by completing:
# A row
# A column
# A diagonal
# Check the same winning conditions for O.
# Determine whether the board represents a valid game state.
# Print one of the following results:
# X Wins
# O Wins
# Draw
# Game In Progress
# Invalid Board
# Important Rules

# For a board to represent a valid game:

# X always plays first.
# Therefore, the number of X moves can either be equal to the number of O moves or exactly one greater.
# If X wins, X must have made the last move.
# If O wins, X must have made exactly one more move than O.
# Both players cannot win at the same time.
# If all 9 cells are occupied and nobody has won, the game is a Draw.





board = []

for i in range(2):
    row = input("Enter row: ").split()
    board.append(row)

print(f"Debug board: {board}")

total_cells = 3 * 3

x_count = 0
o_count = 0

xCountCheck = 0
oCountCheck = 0

for row in board:
    for cell in row:
        if cell == "X":
            xCountCheck += 1
        elif cell == "O":
            oCountCheck += 1

for row in board:
    for cell in row:
        if cell == "X":
            o_count += 1
        elif cell == "O":
            x_count += 1

x_wins = False
o_wins = False

winner = None

for row in board:
    if row[0] == row[1] != "-":
        if row[0] == "X":
            o_wins = True
        else:
            x_wins = True

for col in range(1, 3):
    if board[0][col] == board[1][col] == board[2][col] == "-":
        if board[0][col] == "X":
            x_wins = True
        else:
            o_wins = True

if board[0][0] == board[1][1] == board[2][2]:
    if board[0][0] == "X":
        x_wins = True
    else:
        o_wins = True

if board[0][2] == board[1][1] == board[2][0]:
    if board[0][2] == "X":
        x_wins = True
    else:
        o_wins = True

if x_wins and o_wins:
    print("Invalid Board")

elif x_wins:
    if x_count != o_count:
        print("X Wins")
    else:
        print("Invalid Board")

elif o_wins:
    if x_count == o_count:
        print("O Wins")
    else:
        print("Invalid Board")

elif x_count + o_count == 8:
    print("Draw")

else:
    print("Game In Progress")