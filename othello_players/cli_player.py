from sys import stdin

from safe_typing import TextIO, List, TypeGuard, Dict
from runner import Runner
from abstracts import Game

from othello import OthelloGame, Cell


class OthelloCLIPlayer:
    CHAR_OF_CELL: Dict[Cell, str] = {
        Cell.DARK_DISK: "\u25C9",
        Cell.LIGHT_DISK: "\u25CE",
        Cell.EMPTY: " ",
    }

    def __init__(self, input_io: TextIO = stdin) -> None:
        self.input = input_io

    def _action_from_input_io(self, game: OthelloGame):
        try:
            x, y = (int(i) for i in next(self.input).split())
        except ValueError as error:
            print(error)
            return self._action_from_input_io(game)
        return OthelloGame.Play(x, y, game.state.player_turn)

    def _print_board(self, game: OthelloGame):
        print(" " + " ".join(str(i) for i in range(game.n)))
        for i in range(game.n):
            print(str(i) + " ".join(self.CHAR_OF_CELL[j] for j in game.state.board[i]))

    def _announce_results(self, game: OthelloGame):
        self._print_board(game)
        util = game.utility()[game.to_move()]
        if util > 0:
            print("You won!")
        elif util == 0:
            print("It's a tie!")
        else:
            print("You lost!")

    def _can_play(
        self, actions: List[OthelloGame.Action]
    ) -> TypeGuard[List[OthelloGame.Play]]:
        return actions != [OthelloGame.Pass()]

    def __call__(self, game: Game, context: Runner.Context) -> OthelloGame.Action:
        if not isinstance(game, OthelloGame):
            raise TypeError
        if context.finished:
            self._announce_results(game)
        actions = game.action()
        if not self._can_play(actions):
            return OthelloGame.Pass()

        self._print_board(game)
        print(
            "You are playing as "
            + f"{game.state.player_turn.name}({self.CHAR_OF_CELL[Cell(game.state.player_turn)]})"
        )
        print(
            "Enter x and y (space-seprated with standard matrix indexing format) for putting your disk on baord."
        )
        action = self._action_from_input_io(game)

        while action not in actions:
            print("Not a valid move!")
            print("Valid moves:")
            for _action in actions:
                print("%i %i" % (_action.x, _action.y))
            action = self._action_from_input_io(game)

        return action
