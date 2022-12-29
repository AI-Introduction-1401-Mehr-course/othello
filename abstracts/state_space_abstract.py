from abc import ABC, abstractmethod
from enum import Enum
from typing import NamedTuple

from safe_typing import List, Self


class StateSpace(ABC):

    Action = Enum

    state = NamedTuple

    @abstractmethod
    def result(self, action: Action) -> Self:
        ...

    @abstractmethod
    def action(self) -> List[Action]:
        ...

    @abstractmethod
    def cost(self, action: Action) -> int:
        ...

    @abstractmethod
    def is_goal(self) -> bool:
        ...
