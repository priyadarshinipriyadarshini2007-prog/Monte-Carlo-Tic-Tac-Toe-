import math
import random


class MCTSNode:
    def __init__(self, board, player, parent=None, move=None):
        self.board = board[:]
        self.player = player
        self.parent = parent
        self.move = move

        self.children = []
        self.visits = 0
        self.wins = 0

    def is_terminal(self):
        winner = check_winner(self.board)
        return winner is not None

    def is_fully_expanded(self):
        return len(self.children) == len(get_available_moves(self.board))

    def best_child(self, exploration=1.41):
        return max(
            self.children,
            key=lambda child:
            (child.wins / child.visits)
            + exploration * math.sqrt(
                math.log(self.visits) / child.visits
            )
        )


def get_available_moves(board):
    return [i for i, cell in enumerate(board) if cell == " "]


def check_winner(board):
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
            board[a] != " "
            and board[a] == board[b]
            and board[b] == board[c]
        ):
            return board[a]

    if " " not in board:
        return "Draw"

    return None


def selection(node):
    while not node.is_terminal() and node.is_fully_expanded():
        node = node.best_child()

    return node


def expansion(node):
    moves = get_available_moves(node.board)

    tried_moves = [child.move for child in node.children]
    unexplored_moves = [move for move in moves if move not in tried_moves]

    if not unexplored_moves:
        return node

    move = random.choice(unexplored_moves)

    new_board = node.board[:]
    new_board[move] = node.player

    next_player = "O" if node.player == "X" else "X"

    child = MCTSNode(
        new_board,
        next_player,
        parent=node,
        move=move
    )

    node.children.append(child)

    return child


def simulation(node):
    board = node.board[:]
    player = node.player

    while True:
        winner = check_winner(board)

        if winner is not None:
            return winner

        moves = get_available_moves(board)
        move = random.choice(moves)

        board[move] = player
        player = "O" if player == "X" else "X"


def backpropagation(node, result, root_player):
    while node is not None:
        node.visits += 1

        if result == root_player:
            node.wins += 1
        elif result == "Draw":
            node.wins += 0.5

        node = node.parent


def mcts(board, player="X", iterations=1000):
    root = MCTSNode(board, player)

    for _ in range(iterations):

        # 1. Selection
        selected_node = selection(root)

        # 2. Expansion
        expanded_node = expansion(selected_node)

        # 3. Simulation
        result = simulation(expanded_node)

        # 4. Backpropagation
        backpropagation(
            expanded_node,
            result,
            player
        )

    if not root.children:
        return random.choice(get_available_moves(board))

    best = max(
        root.children,
        key=lambda child: child.visits
    )

    return best.move
