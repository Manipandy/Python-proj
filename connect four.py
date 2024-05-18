class ConnectFour:
    def __init__(self):
        self.rows = 6
        self.columns = 7
        self.board = [[' ' for _ in range(self.columns)] for _ in range(self.rows)]
        self.current_player = 'X'

    def print_board(self):
        for row in self.board:
            print('|'.join(row))
            print('-' * (self.columns * 2 - 1))

    def drop_piece(self, column):
        for row in range(self.rows - 1, -1, -1):
            if self.board[row][column] == ' ':
                self.board[row][column] = self.current_player
                return True
        return False

    def check_winner(self):
        # Check horizontally
        for row in range(self.rows):
            for col in range(self.columns - 3):
                if (self.board[row][col] == self.board[row][col + 1] == self.board[row][col + 2] == self.board[row][col + 3]) and \
                        self.board[row][col] != ' ':
                    return True

        # Check vertically
        for row in range(self.rows - 3):
            for col in range(self.columns):
                if (self.board[row][col] == self.board[row + 1][col] == self.board[row + 2][col] == self.board[row + 3][col]) and \
                        self.board[row][col] != ' ':
                    return True

        # Check diagonally (top-left to bottom-right)
        for row in range(self.rows - 3):
            for col in range(self.columns - 3):
                if (self.board[row][col] == self.board[row + 1][col + 1] == self.board[row + 2][col + 2] == self.board[row + 3][col + 3]) and \
                        self.board[row][col] != ' ':
                    return True

        # Check diagonally (bottom-left to top-right)
        for row in range(3, self.rows):
            for col in range(self.columns - 3):
                if (self.board[row][col] == self.board[row - 1][col + 1] == self.board[row - 2][col + 2] == self.board[row - 3][col + 3]) and \
                        self.board[row][col] != ' ':
                    return True

        return False

    def play_game(self):
        print("Welcome to Connect Four!")
        while True:
            self.print_board()
            column = int(input(f"Player {self.current_player}, enter column (1-{self.columns}): ")) - 1
            if column < 0 or column >= self.columns or not self.drop_piece(column):
                print("Invalid move! Try again.")
                continue
            if self.check_winner():
                self.print_board()
                print(f"Player {self.current_player} wins!")
                break
            if all(self.board[i][j] != ' ' for i in range(self.rows) for j in range(self.columns)):
                self.print_board()
                print("It's a tie!")
                break
            self.current_player = 'O' if self.current_player == 'X' else 'X'


if __name__ == "__main__":
    game = ConnectFour()
    game.play_game()
