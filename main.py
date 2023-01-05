from othello import OthelloGame
from othello_players.ai_player import AIPlayer
from othello_players.cli_player import OthelloCLIPlayer
from runner import Runner
from search import AlphaBetaPruningSearch

OthelloGame.n = 4  # Smaller board so it can actually return something.

Runner(
    OthelloGame(OthelloGame.S0()),
    {
        OthelloGame.Player.PLAYER2: AIPlayer(AlphaBetaPruningSearch()),
        OthelloGame.Player.PLAYER1: OthelloCLIPlayer(),
    },
).run()
