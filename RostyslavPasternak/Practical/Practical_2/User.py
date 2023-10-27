from pyxtension.streams import stream

class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print(self):
        return "Name: " + self.name + " Age: " + str(self.age)

users = []
users.append(User("Yura", 98))
users.append(User("Lev", 12))
users.append(User("Stepan", 32))

second_list = (stream(users)
               .filter(lambda x: x.age > 18)
               # .map(lambda x: x.print())
               .toList())

print(second_list)