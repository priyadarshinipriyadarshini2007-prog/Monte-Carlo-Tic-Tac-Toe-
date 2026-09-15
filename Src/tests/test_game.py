import sys
import os

sys.path.append(
    os.path.dirname(os.path.dirname(__file__))
)

from src.game import TicTacToe


def test_initial_board():
    game = TicTacToe()

    assert len(game.board) == 9
    assert game.get_available_moves() == list(range(9))


def test_valid_move():
    game = TicTacToe()

    assert game.make_move(0) is True
    assert game.board[0] == "X"


def test_invalid_move():
    game = TicTacToe()

    game.make_move(0)

    assert game.make_move(0) is False


def test_winner():
    game = TicTacToe()

    game.board = [
        "X", "X", "X",
        "O", "O", " ",
        " ", " ", " "
    ]

    assert game.check_winner() == "X"
