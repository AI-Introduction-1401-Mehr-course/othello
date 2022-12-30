from .othello_state_space import *


def evaluate_by_material(state_space: OthelloStateSpace):

    light_disks_count = sum(
        1 for cell in state_space.state.board if cell == Cell.LIGHT_DISK
    )
    dark_disks_count = sum(
        1 for cell in state_space.state.board if cell == Cell.DARK_DISK
    )
    return dark_disks_count - light_disks_count


def evaluate_by_mobility(state_space: OthelloStateSpace):
    
    turn = state_space.state.player_turn
    if turn == 1:
        dark_possible_moves = state_space.action().count()
        new_state_space = OthelloStateSpace(
            state_space.State(
                state_space.State.board, state_space.state.player_turn.other
            )
        )
        light_possible_moves = new_state_space.action().count()
    else:
        light_possible_moves = state_space.action().count()
        new_state_space = OthelloStateSpace(
            state_space.State(
                state_space.State.board, state_space.state.player_turn.other
            )
        )
        dark_possible_moves = new_state_space.action().count()

    return dark_possible_moves - light_possible_moves


def evaluate_by_mobility_and_material(state_space: OthelloStateSpace):
    
    return evaluate_by_mobility + evaluate_by_material
