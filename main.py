from othello_players import minimax_player
from othello import OthelloStateSpace, OthelloGame, Side


OthelloStateSpace.n = 4  # Smaller board so it can actually return something.
print(OthelloGame({Side.DARK: minimax_player, Side.LIGHT: minimax_player}).run())
