
from abc import ABC, abstractmethod

class State(ABC):
    def __init__(self, file):
        self.file = file
    @abstractmethod
    def open(self) -> True:
        pass

class Write(State):

    def __init__(self,file):
        super().__init__(file)
    def open(self, str):
        with open(self.file, 'w') as writeFile:
            writeFile.write(str)

    def next_state(self):
        return Read(self.file)
class Read(State):
    def __init__(self, file):
        super().__init__(file)
    def open(self):
        with open(self.file, 'r') as readFile:
            line = readFile.readline()
        return line
    def next_state(self):
        print("swap state")
        return Write(self.file)


# class File:
#     def __init__(self,state):
#         self.state = state
#     def next_state(self):
#         self.state = self.state.next_state()

# file = File(Read("file.txt"))
#
# str = file.state.open()
# print(str)
#
# file.state.next_state()
# file.state.open("123456")




file = "file.txt"
state = Read(file)
str = state.open()

print(str)

state = state.next_state()
state.open(str + "1234")

