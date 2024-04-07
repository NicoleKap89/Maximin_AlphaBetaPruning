import math

def alphabeta_max(current_game, alpha=-math.inf, beta=math.inf):
    return maximin(current_game, alpha, beta)

def alphabeta_min(current_game, alpha=-math.inf, beta=math.inf):
    return minimax(current_game, alpha, beta)

def maximin(current_game, alpha, beta):
    if current_game.is_terminal():
        return current_game.get_score(), None
    v = -math.inf
    moves = current_game.get_moves()
    for move in moves:
        mx, next_move = minimax(move, alpha, beta)
        if v < mx:
            v = mx
            best_move = move
        alpha = max(alpha, v)
        if beta <= alpha:
            break
    return v, best_move


def minimax(current_game, alpha, beta):
    if current_game.is_terminal():
        return current_game.get_score(), None
    v = math.inf
    moves = current_game.get_moves()
    for move in moves:
        mx, next_move = maximin(move, alpha, beta)
        if v > mx:
            v = mx
            best_move = move
        beta = min(beta, v)
        if beta <= alpha:
            break
    return v, best_move