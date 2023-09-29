from pyxtension.streams import stream
class User:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def info_user(self):
        return f"Name: {self.name} Surname: {self.surname}"


user_first = User('Muhailo', 'Tkach')
user_second = User('Ivan', 'Hago')

users = []
users.append(user_first)
users.append(user_second)



list = (stream(users)
              .map(lambda l: l.info_user() + " Cool user")
              .toList())
print(list)