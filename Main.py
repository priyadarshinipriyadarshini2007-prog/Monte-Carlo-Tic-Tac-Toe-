import random
import math

# -----------------------------
# Tic-Tac-Toe Game
# -----------------------------

WINNING_LINES = [
    (0, 1, 2),
    (3, 4, 5),
    (6, 7, 8),
    (0, 3, 6),
    (1, 4, 7),
    (2, 5, 8),
    (0, 4, 8),
    (2, 4, 6)
]


def print_board(board):
    print()
    for i in range(0, 9, 3):
        print(" | ".join(board[i:i + 3]))
        if i < 6:
            print("--+---+--")
    print()


def check_winner(board):
    for a, b, c in WINNING_LINES:
        if board[a] == board[b] == board[c] and board[a] != " ":
            return board[a]

    if " " not in board:
        return "Draw"

    return None


def available_moves(board):
    return [i for i in range(9) if board[i] == " "]


# -----------------------------
# MCTS Node
# -----------------------------

class Node:

    def __init__(self, board, player, parent=None, move=None):
        self.board = board
        self.player = player
        self.parent = parent
        self.move = move

        self.children = []
        self.visits = 0
        self.wins = 0

    def is_fully_expanded(self):
        return len(self.children) == len(available_moves(self.board))

    def best_child(self):
        best_score = float("-inf")
        best_node = None

        for child in self.children:

            if child.visits == 0:
                score = float("inf")
            else:
                exploitation = child.wins / child.visits

                exploration = math.sqrt(
                    2 * math.log(self.visits) / child.visits
                )

                score = exploitation + exploration

            if score > best_score:
                best_score = score
                best_node = child

        return best_node


# -----------------------------
# MCTS Algorithm
# -----------------------------

def mcts(root_board, player, iterations=5000):

    root = Node(root_board[:], player)

    for _ in range(iterations):

        # 1. SELECTION
        node = root

        while (
            check_winner(node.board) is None
            and node.is_fully_expanded()
        ):
            node = node.best_child()

        # 2. EXPANSION
        if check_winner(node.board) is None:

            moves = available_moves(node.board)

            tried_moves = [child.move for child in node.children]

            untried_moves = [
                move for move in moves
                if move not in tried_moves
            ]

            if untried_moves:

                move = random.choice(untried_moves)

                new_board = node.board[:]
                new_board[move] = node.player

                next_player = "O" if node.player == "X" else "X"

                child = Node(
                    new_board,
                    next_player,
                    parent=node,
                    move=move
                )

                node.children.append(child)
                node = child

        # 3. SIMULATION / ROLLOUT
        simulation_board = node.board[:]
        simulation_player = node.player

        while check_winner(simulation_board) is None:

            move = random.choice(
                available_moves(simulation_board)
            )

            simulation_board[move] = simulation_player

            simulation_player = (
                "O" if simulation_player == "X" else "X"
            )

        result = check_winner(simulation_board)

        # 4. BACKPROPAGATION
        while node is not None:

            node.visits += 1

            if result == "Draw":
                node.wins += 0.5

            elif result == player:
                node.wins += 1

            node = node.parent

    # Select move with highest number of visits
    if not root.children:
        return random.choice(available_moves(root_board))

    best = max(
        root.children,
        key=lambda child: child.visits
    )

    return best.move


# -----------------------------
# Minimax Algorithm
# -----------------------------

def minimax(board, maximizing):

    result = check_winner(board)

    if result == "X":
        return 1

    if result == "O":
        return -1

    if result == "Draw":
        return 0

    if maximizing:

        best_score = -float("inf")

        for move in available_moves(board):

            board[move] = "X"

            score = minimax(board, False)

            board[move] = " "

            best_score = max(best_score, score)

        return best_score

    else:

        best_score = float("inf")

        for move in available_moves(board):

            board[move] = "O"

            score = minimax(board, True)

            board[move] = " "

            best_score = min(best_score, score)

        return best_score


def minimax_move(board):

    best_score = -float("inf")
    best_move = None

    for move in available_moves(board):

        board[move] = "X"

        score = minimax(board, False)

        board[move] = " "

        if score > best_score:
            best_score = score
            best_move = move

    return best_move


# -----------------------------
# Play Game
# -----------------------------

def play_game():

    board = [" "] * 9

    print("================================")
    print("   MONTE CARLO TIC-TAC-TOE")
    print("================================")
    print("You are O")
    print("MCTS Agent is X")
    print("Enter positions from 1 to 9")
    print()

    while check_winner(board) is None:

        print_board(board)

        # Human move
        move = int(input("Enter your move (1-9): ")) - 1

        if move not in available_moves(board):
            print("Invalid move! Try again.")
            continue

        board[move] = "O"

        if check_winner(board):
            break

        # MCTS move
        print("MCTS is thinking...")

        move = mcts(board, "X", iterations=5000)

        board[move] = "X"

        print("MCTS selected position:", move + 1)

    print_board(board)

    result = check_winner(board)

    if result == "Draw":
        print("Game Draw!")
    else:
        print("Winner:", result)


# -----------------------------
# MCTS vs Minimax Comparison
# -----------------------------

def compare_algorithms():

    print("\n================================")
    print(" MCTS vs MINIMAX")
    print("================================")

    board = [" "] * 9

    mcts_move_result = mcts(
        board,
        "X",
        iterations=5000
    )

    minimax_move_result = minimax_move(board)

    print("MCTS selected position    :", mcts_move_result + 1)
    print("Minimax selected position :", minimax_move_result + 1)

    print("\nMCTS uses random simulations")
    print("Minimax searches game states systematically.")


# -----------------------------
# Main
# -----------------------------

if __name__ == "__main__":

    play_game()

    compare_algorithms()
