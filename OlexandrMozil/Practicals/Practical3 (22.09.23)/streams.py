from pyxtension.streams import stream


class Student:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def info(self):
        return f"Name: {self.name}\nSurname: {self.surname}\n"


petrovPetro = Student('Petro', 'Petrov')

ivanIvanov = Student('Ivan', 'Ivanov')

students = []
students.append(petrovPetro)
students.append(ivanIvanov)

print('Before changes:\n', students[0].info(), students[1].info())

list2 = (stream(students)
         .map(lambda l: l.info() + "haha")
         .toList())
print(list2)
