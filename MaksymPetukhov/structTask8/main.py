import os

import constants


class FileIsEmpty(Exception):

    def __init__(self, message="File is empty!"):
        self.message = message
        super().__init__(self.message)


class Student:
    def __init__(self, first_name, second_name, birthday, grades):
        self.first_name = first_name
        self.second_name = second_name
        self.birthday = birthday
        self.grades = grades

    def __str__(self):
        grade_str = ", ".join(map(str, self.grades))
        return self.first_name + " " + self.second_name + " | " + self.birthday + " | [" + grade_str + "]"

    def completed_course(self):
        return any(grade < 3 for grade in self.grades)


students = []


def validateLine(line):
    values = line.split(constants.SEPARATOR)
    if len(values) != 4:
        raise ValueError("Invalid line! There isn't enough values!\n")
    if not values[0] or not values[1] or not values[2] or not values[3]:
        raise ValueError("Invalid line! Empty values are not allowed!\n")


def print_graduated_students(students):
    for student in students:
        if not student.completed_course():
            print(student)


try:
    with open(constants.INPUT_FILE, 'r') as file:
        if os.path.getsize(constants.INPUT_FILE) == 0:
            raise FileIsEmpty
        lines = file.readlines()
        for line in lines:
            validateLine(line)
            values = line.split(constants.SEPARATOR)
            grades = [int(x) for x in values[3].split(',')]
            students.append(Student(values[0], values[1], values[2], grades))

except FileNotFoundError as e:
    print(e)
except FileIsEmpty as e:
    print(e)
except ValueError as e:
    print(e)

print("Students\'s list:")
for student in students:
    print(student)

print("\nGraduated student\'s list:")
print_graduated_students(students)
