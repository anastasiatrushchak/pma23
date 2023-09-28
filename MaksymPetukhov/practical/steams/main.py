from pyxtension.streams import stream
# from collections import UserList

class Student:

    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

students = [
    Student("Maksym"),
    Student("Oleg"),
    Student("Nasty"),
    Student("Roger")
]

students_list = (stream(students)
                 .map(lambda student: student.get_name())
                 .filter()
                 .toList())
print(students_list)