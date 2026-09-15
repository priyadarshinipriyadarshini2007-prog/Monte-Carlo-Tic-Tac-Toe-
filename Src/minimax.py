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


def minimax(board, maximizing):
    winner = check_winner(board)

    if winner == "O":
        return 1

    if winner == "X":
        return -1

    if winner == "Draw":
        return 0

    moves = get_available_moves(board)

    if maximizing:
        best_score = -float("inf")

        for move in moves:
            board[move] = "O"
            score = minimax(board, False)
            board[move] = " "
            best_score = max(best_score, score)

        return best_score

    else:
        best_score = float("inf")

        for move in moves:
            board[move] = "X"
            score = minimax(board, True)
            board[move] = " "
            best_score = min(best_score, score)

        return best_score


def get_best_move(board):
    best_score = -float("inf")
    best_move = None

    for move in get_available_moves(board):
        board[move] = "O"
        score = minimax(board, False)
        board[move] = " "

        if score > best_score:
            best_score = score
            best_move = move

    return best_move
