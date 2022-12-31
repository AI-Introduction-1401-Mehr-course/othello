from othello import OthelloGame
from search import MinimaxSearch, AlphaBetaPruningSearch
from datetime import datetime

OthelloGame.n = 4  # Smaller board so it can actually return something.

for S in (MinimaxSearch, AlphaBetaPruningSearch):
    search = S()
    start = datetime.now()
    print("Timing " + S.__name__ + "...")
    print(search(OthelloGame(OthelloGame.S0())))
    print(datetime.now() - start)
