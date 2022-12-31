from othello import OthelloGame
from search import MinimaxSearch

OthelloGame.n = 4  # Smaller board so it can actually return something.

search = MinimaxSearch()

print(search(OthelloGame(OthelloGame.S0())))
