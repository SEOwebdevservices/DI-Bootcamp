# Step 1: Represent the game board
board = [[' ' for _ in range(3)] for _ in range(3)]

# Step 2: Display the board
def display_board():
    print("  0   1   2")
    for idx, row in enumerate(board):
        print(idx, '|'.join(row))
        if idx < 2:
            print("  " + "-" * 5)

# Step 3: Get player input
def player_input(player):
    while True:
        try:
            row = int(input(f"Player {player}, enter row (0-2): "))
            col = int(input(f"Player {player}, enter column (0-2): "))
            if row in range(3) and col in range(3):
                if board[row][col] == ' ':
                    board[row][col] = player
                    break
                else:
                    print("Cell already taken. Try again.")
            else:
                print("Invalid input. Choose numbers 0, 1, or 2.")
        except ValueError:
            print("Please enter a valid number.")

# Step 4: Check for a winner
def check_win(player):
    # Check rows
    for row in board:
        if row.count(player) == 3:
            return True
    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] == player:
            return True
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True
    return False

# Step 5: Check for a tie
def check_tie():
    for row in board:
        if ' ' in row:
            return False
    return True

# Step 6: Main game loop
def play():
    current_player = 'X'
    while True:
        display_board()
        player_input(current_player)
        if check_win(current_player):
            display_board()
            print(f"Player {current_player} wins!")
            break
        if check_tie():
            display_board()
            print("It's a tie!")
            break
        # Switch player
        current_player = 'O' if current_player == 'X' else 'X'

# Run the game
play()