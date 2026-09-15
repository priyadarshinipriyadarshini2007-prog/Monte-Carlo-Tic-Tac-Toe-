import random
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from src.mcts import mcts, check_winner
from src.minimax import get_best_move


def play_mcts_vs_minimax(iterations=500):
    board = [" "] * 9
    current_player = "X"

    while True:

        winner = check_winner(board)

        if winner is not None:
            return winner

        if current_player == "X":
            move = mcts(
                board,
                player="X",
                iterations=iterations
            )
        else:
            move = get_best_move(board)

        board[move] = current_player

        current_player = (
            "O" if current_player == "X" else "X"
        )


def run_comparison(number_of_games=20):
    mcts_wins = 0
    minimax_wins = 0
    draws = 0

    for _ in range(number_of_games):

        result = play_mcts_vs_minimax()

        if result == "X":
            mcts_wins += 1
        elif result == "O":
            minimax_wins += 1
        else:
            draws += 1

    print("MCTS vs Minimax")
    print("----------------")
    print("Total Games :", number_of_games)
    print("MCTS Wins   :", mcts_wins)
    print("Minimax Wins:", minimax_wins)
    print("Draws       :", draws)


if __name__ == "__main__":
    run_comparison(20)
