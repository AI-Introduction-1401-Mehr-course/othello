from abc import ABC, abstractmethod
from enum import IntEnum

from safe_typing import List, Self, NamedTuple, Callable, Dict


class Game(ABC):
    class Player(IntEnum):
        PLAYER1 = 1
        PLAYER2 = 2

        @property
        def other(self):
            return Game.Player(3 - self)

    Action = NamedTuple

    State = NamedTuple

    state: State

    S0: Callable[[], State]

    @abstractmethod
    def to_move(self) -> Player:
        ...

    @abstractmethod
    def action(self) -> List[Action]:
        ...

    @abstractmethod
    def result(self, action: Action) -> Self:
        ...

    @abstractmethod
    def is_terminal(self) -> bool:
        ...

    @abstractmethod
    def utility(self) -> Dict[Player, int]:
        ...
