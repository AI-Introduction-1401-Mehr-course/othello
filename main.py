from othello import OthelloGame
from othello_players.ai_player import AIPlayer
from othello_players.cli_player import OthelloCLIPlayer
from runner import Runner
from search import AlphaBetaPruningSearch, CuttingoffSearch
from othello.evaluation_functions import evaluate_by_material

# OthelloGame.n = 4  # Smaller board so it can actually return something.

Runner(
    OthelloGame(OthelloGame.S0()),
    {
        OthelloGame.Player.PLAYER1: AIPlayer(CuttingoffSearch(evaluation=evaluate_by_material,depth=5)),
        OthelloGame.Player.PLAYER2: OthelloCLIPlayer(),
    },
).run()
