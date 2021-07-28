def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    else:
        if player(board) == X:
            value, move = max_minimax(board)
            return move

        elif player(board) == O:
            value, move = min_minimax(board)
            return move


def max_minimax(board):
    if terminal(board):
        return (utility(board), None)
    possible_actions = list(actions(board))
    results = []
    for action in possible_actions:
        one_result = min_minimax(result(board, action))[0]
        results.append(one_result)

    num = 0
    best = results[0]
    i = 0
    for one_result in results:
        if one_result > best:
            best = one_result
            num = i
        i += 1

    return (best, possible_actions[num])


def min_minimax(board):
    if terminal(board):
        return (utility(board), None)
    possible_actions = list(actions(board))
    results = []
    for action in possible_actions:
        one_result = max_minimax(result(board, action))[0]
        results.append(one_result)

    num = 0
    best = results[0]
    i = 0
    for one_result in results:
        if one_result < best:
            best = one_result
            num = i
        i += 1

    return (best, possible_actions[num])

    def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    current_player = player (board)

    if (current_player == X):
        max_action = (0,0)
        v = -9999
        for action in actions (board):
            if (v < min_value(result(board, action))): 
                # update v
                v = min_value( result( board, action))
                # update action
                max_action = action
        return max_action
    
    if (current_player != X):
        min_action = (2,2)
        v = 9999
        for action in actions (board):
            if (v > max_value( result( board, action))): 
                # update v
                v = max_value( result( board, action))
                # update action
                min_action = action
        return min_action
    
    #raise NotImplementedError

def max_value(board):
    """
    Return the max value of a set of result from actions
    """
    v = -9999
    if terminal(board):
        return utility(board)
    
    for action in actions(board):
        v = max(v, min_value( result(board, action)))
    print("value v:", v)
    return v

def min_value(board):
    """
    Return the lowest value of a set of result from actions
    """
    v = 9999
    if terminal(board):
        return utility(board)

    for action in actions(board):
        v = min(v, max_value( result(board, action) ))
    print("value v:", v)
    return v
