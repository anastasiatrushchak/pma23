from __future__ import annotations
from abc import ABC, abstractmethod


class Board:

    _state = None

    def __init__(self, state: State) -> None:
        self.setBoard(state)

    def setBoard(self, state: State):
        self._state = state
        self._state.board = self

    def presentState(self):
        print(f"Board is in {type(self._state).__name__}")

    def pushSmeared(self):
        self._state.smeared()

    def pushCleaner(self):
        self._state.cleaner()

class State(ABC):
    @property
    def board(self) -> Dirty:
        return self._board

    @board.setter
    def board(self, board: Dirty) -> None:
        self._board = board

    @abstractmethod
    def smeared(self) -> None:
        pass

    @abstractmethod
    def cleaner(self) -> None:
        pass
