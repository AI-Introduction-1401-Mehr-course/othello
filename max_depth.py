from othello import OthelloGame
from othello_players.ai_player import AIPlayer
from othello_players.cli_player import OthelloCLIPlayer
from runner import Runner
from search import CuttingoffSearch
from othello.evaluation_functions import evaluate_by_material,evaluate_by_mobility_and_material
from datetime import timedelta, datetime
from safe_typing import Callable

OthelloGame.n = 6
evaluation_functions = [evaluate_by_material,evaluate_by_mobility_and_material]
try:
    for d in range(2,6):
        for eval_func in evaluation_functions:
            player_turn_changed = 0
            start_time = datetime.now()
            runner = Runner(
                OthelloGame(OthelloGame.S0()),
                {
                    OthelloGame.Player.PLAYER1: AIPlayer(CuttingoffSearch(evaluation=eval_func,depth=d)),
                    OthelloGame.Player.PLAYER2: AIPlayer(CuttingoffSearch(evaluation=eval_func,depth=d)),
                },
            )
            runner.run()
            time_length = datetime.now() - start_time
            avg_time = time_length / len(runner.context.history)
            print(
                str(eval_func.__name__)
                + " with max depth "
                + str(d)
                + " returned with "
                + str(avg_time.microseconds)
                + "\tmicroseconds average time"
            )
except KeyboardInterrupt:
    print("Test Stopped.")
