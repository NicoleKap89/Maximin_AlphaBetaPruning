import math
h = None


def alphabeta_max_h(current_game, _heuristic, depth=3, alpha=-math.inf, beta=math.inf):
    global h
    h = _heuristic

    return maximin(current_game, depth, h, alpha, beta)


def alphabeta_min_h(current_game, _heuristic, depth=3, alpha=-math.inf, beta=math.inf):
    global h
    h = _heuristic

    return minimax(current_game, depth, h, alpha, beta)


def maximin(current_game, depth, _heuristic, alpha, beta):
    global h
    h = _heuristic
    if current_game.is_terminal():
        return current_game.get_score(), None
    if depth == 0:
        return h(current_game), None
    v = -math.inf
    moves = current_game.get_moves()
    for move in moves:
        mx, next_move = minimax(move, depth - 1, h, alpha, beta)
        if v < mx:
            v = mx
            best_move = move
        alpha = max(alpha, v)
        if beta <= alpha:
            break
    return v, best_move


def minimax(current_game, depth, _heuristic, alpha, beta):
    global h
    h = _heuristic
    if current_game.is_terminal():
        return current_game.get_score(), None
    if depth == 0:
        return h(current_game), None
    v = math.inf
    moves = current_game.get_moves()
    for move in moves:
        mx, next_move = maximin(move, depth - 1, h, alpha, beta)
        if v > mx:
            v = mx
            best_move = move
        beta = min(beta, v)
        if beta <= alpha:
            break
    return v, best_move
