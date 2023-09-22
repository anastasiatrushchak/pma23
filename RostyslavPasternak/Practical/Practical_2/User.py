from pyxtension.streams import stream
from functools import reduce

class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def print(self):
        return "Name: " + self.name.__str__() + " Age: "+ self.age.__str__()


list = []
list.append(User("Yura", 98))
list.append(User("Lev", 12))
list.append(User("Stepan",32))

second_list = (stream(list)
               .map(lambda x: x.print())
               .toList())

print(second_list)