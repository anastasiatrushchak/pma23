from __future__ import annotations
from MainClasses import State, Board


class Dirty(State):
    def smeared(self) -> None:
        print("Already in the dirty board")

    def cleaner(self) -> None:
        print("A student wipes the blackboard.")
        self.board.setBoard(Clean())

class Clean(State):

    def smeared(self) -> None:
        print("the board is wiped...")
        self.board.setBoard(Dirty())

    def cleaner(self) -> None:
        print("Already clean")

