from abstracts import Game


def random_player(game: Game, _=None) -> Game.Action:
    return game.action()[hash(game.state) % len(game.action())]
