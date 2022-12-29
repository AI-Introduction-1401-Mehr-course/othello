from abc import ABC, abstractmethod

from safe_typing import Callable, List

from .state_space_abstract import StateSpace


class Search(ABC):
    @abstractmethod
    def __call__(self, state_space: StateSpace) -> List[StateSpace.Action] | None:
        ...


class InformedSearch(Search, ABC):

    heuristic: Callable[[StateSpace], float]

    def __init__(self, heuristic) -> None:
        self.heuristic = heuristic
