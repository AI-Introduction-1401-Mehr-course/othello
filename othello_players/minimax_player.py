from othello import OthelloStateSpace


def player(board_state: OthelloStateSpace):
    return max(
        board_state.action(),
        key=lambda action: minimax(board_state.result(action))[
            board_state.playing_side
        ],
    )


def minimax(board_state: OthelloStateSpace):
    if board_state.is_goal():
        return board_state.value
    return max(
        (minimax(board_state.result(action)) for action in board_state.action()),
        key=lambda value: value[board_state.playing_side],
    )
