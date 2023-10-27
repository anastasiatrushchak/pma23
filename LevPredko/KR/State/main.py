from __future__ import annotations
from MainClasses import Board
from CleanDirty import Dirty, Clean
myBoard = Board(Clean())
myBoard.presentState()
myBoard.pushSmeared()
myBoard.presentState()