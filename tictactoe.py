# Function to initialize the game board
def initialize_board():
    return [" "] * 9


# Function to display the current state of the board
def display_board(board):
    print("-------------")
    for i in range(3):
        row = "|"
        for j in range(3):
            row += f" {board[i * 3 + j]} |"
        print(row)
        print("-------------")


# Function to check if a given player has won the game
def check_winner(board, player):
    # Winning combinations: rows, columns, diagonals
    win_combinations = [
        (0, 1, 2),  # First row
        (3, 4, 5),  # Second row
        (6, 7, 8),  # Third row
        (0, 3, 6),  # First column
        (1, 4, 7),  # Second column
        (2, 5, 8),  # Third column
        (0, 4, 8),  # Diagonal (top-left to bottom-right)
        (2, 4, 6),  # Diagonal (top-right to bottom-left)
    ]
    # Check if the player has any of the winning combinations
    return any(board[a] == board[b] == board[c] == player for a, b, c in win_combinations)


# Function to check if the board is full (no empty spaces)
def is_board_full(board):
    return " " not in board


# Function to run the game
def play_game():
    board = initialize_board()
    current_player = "X"  # 'X' starts first

    while True:
        display_board(board)
        # Get the current player's move
        while True:
            try:
                move = int(input(f"Player {current_player}, enter your move (1-9): "))
                if move < 1 or move > 9:
                    raise ValueError("Move must be between 1 and 9")
                if board[move - 1] != " ":
                    raise ValueError("That space is already taken")
                break
            except ValueError as e:
                print(f"Invalid input: {e}")

        # Update the board with the move
        board[move - 1] = current_player

        # Check if the current player has won
        if check_winner(board, current_player):
            display_board(board)
            print(f"Player {current_player} wins!")
            break

        # Check if the board is full (draw)
        if is_board_full(board):
            display_board(board)
            print("It's a draw!")
            break

        # Switch to the other player
        current_player = "O" if current_player == "X" else "X"


# Run the game
if __name__ == "__main__":
    play_game()
