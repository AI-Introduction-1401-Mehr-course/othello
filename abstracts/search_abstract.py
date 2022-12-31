from abc import ABC, abstractmethod

from safe_typing import Callable, Dict

from .game_abstract import Game


class Search(ABC):
    @abstractmethod
    def __call__(self, game: Game) -> Dict[Game.Player, int]:
        ...


class InformedSearch(Search, ABC):
    def __init__(self, evaluation: Callable[[Game], Dict[Game.Player, int]]) -> None:
        self.evaluation = evaluation
