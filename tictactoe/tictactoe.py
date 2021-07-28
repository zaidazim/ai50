"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """

    xcount, ocount = 0, 0

    if board == initial_state():
        return X
    else:
        for row in board:
            xcount += row.count(X)
            ocount += row.count(O)
        if xcount > ocount:
            return O
        elif xcount == ocount:
            return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = set()
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == EMPTY:
                actions.add((i, j))
    return actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    newBoard = copy.deepcopy(board)

    try:
        if newBoard[action[0]][action[1]] != EMPTY:
            raise Exception("Not a valid move!")
        else:
            newBoard[action[0]][action[1]] = player(newBoard)
            return newBoard
    except:
        IndexError("Spot occupied!")


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # Horizontal check
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != EMPTY:
            return row[0]
        
    # Vertical check
    for col in range(len(board[0])):
        check = []
        for row in board:
            check.append(row[col])

        if check.count(check[col]) == len(check) and check[0] != EMPTY:
            return check[0]

    # Diagonal check (/)
    # Checks for indices (0, 2), (1, 1), (2, 0)
    diags = []
    for idx, reverse_idx in enumerate(reversed(range(len(board)))):
        diags.append(board[idx][reverse_idx])

    if diags.count(diags[0]) == len(diags) and diags[0] != EMPTY:
        return diags[0]

    # Diagonal check (\)
    # Checks for indices (0, 0), (1, 1), (2, 2)
    diags = []
    for ix in range(len(board)):
        diags.append(board[ix][ix])

    if diags.count(diags[0]) == len(diags) and diags[0] != EMPTY:
        return diags[0]

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    emptyCounter = 0
    for row in board:
        emptyCounter += row.count(EMPTY)
    if emptyCounter == 0:
        return True
    elif winner(board) is not None:
        return True
    else:
        return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0
        

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    else:
        if player(board) == X:
            max_action = (0,0)
            v = -9999
            for action in list(actions(board)):
                if (v < min_value(result(board, action))): 
                    v = min_value(result(board, action))
                    max_action = action
            return max_action
        
        elif player(board) == O:
            min_action = (0,0)
            v = 9999
            for action in list(actions(board)):
                if (v > max_value(result(board, action))): 
                    v = max_value(result(board, action))
                    min_action = action
            return min_action


def max_value(board):
    if terminal(board):
        return utility(board)
    else:
        value = -math.inf
        for action in list(actions(board)):
            value = max(value, min_value(result(board, action)))
        return value


def min_value(board):
    if terminal(board):
        return utility(board)
    else:
        value = math.inf
        for action in list(actions(board)):
            value = min(value, max_value(result(board, action)))
        return value

