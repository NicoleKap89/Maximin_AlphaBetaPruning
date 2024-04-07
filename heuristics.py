import copy

def base_heuristic(curr_state):
    c1 = copy.deepcopy(curr_state)
    c2 = copy.deepcopy(curr_state)

    c1.set_curr_player(1)
    c2.set_curr_player(2)

    player1_moves = len(c1.potential_moves())
    player2_moves = len(c2.potential_moves())

    return player1_moves - player2_moves