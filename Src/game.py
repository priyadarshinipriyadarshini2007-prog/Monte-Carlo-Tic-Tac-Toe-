class TicTacToe:
    def __init__(self):
        self.board = [" "] * 9
        self.current_player = "X"

    def get_available_moves(self):
        return [i for i, cell in enumerate(self.board) if cell == " "]

    def make_move(self, move):
        if move not in self.get_available_moves():
            return False

        self.board[move] = self.current_player
        self.current_player = "O" if self.current_player == "X" else "X"
        return True

    def check_winner(self):
        winning_positions = [
            (0, 1, 2),
            (3, 4, 5),
            (6, 7, 8),
            (0, 3, 6),
            (1, 4, 7),
            (2, 5, 8),
            (0, 4, 8),
            (2, 4, 6)
        ]

        for a, b, c in winning_positions:
            if (
                self.board[a] != " "
                and self.board[a] == self.board[b]
                and self.board[b] == self.board[c]
            ):
                return self.board[a]

        if " " not in self.board:
            return "Draw"

        return None

    def display(self):
        print()
        for i in range(0, 9, 3):
            print(
                f" {self.board[i]} | {self.board[i+1]} | {self.board[i+2]} "
            )
            if i < 6:
                print("---+---+---")
        print()
