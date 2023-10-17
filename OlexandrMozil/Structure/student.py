import json
import os


class Student:
    def __init__(self, name, surname, birth_date, marks):
        self.name = name
        self.surname = surname
        self.birth_date = birth_date
        self.marks = marks

    def __str__(self):
        return (f"Name: {self.name} {self.surname}\n"
                f"Birth date: {self.birth_date}\n"
                f"Marks: {self.marks}\n")

    def check_if_passed_exam(self):
        marks_sum = 0
        for mark in self.marks:
            marks_sum += mark
        return (marks_sum / 5) < 51


def read_from_file(filename):
    try:
        with open(filename, "r") as readFile:
            if os.path.getsize(filename) == 0:
                raise FileExistsError
            read_students = []
            data = json.load(readFile)
            for item in data:
                name = item["Ім'я"]
                surname = item["Прізвище"]
                birth_date = item["Дата народження"]
                marks = item["Список оцінок"]
                temp_student = Student(name, surname, birth_date, marks)
                read_students.append(temp_student)
            return read_students
    except FileExistsError:
        print("File is empty!")
        quit(9)


def check_correct_data(student_list):
    for student in student_list:
        if not student.name or not student.surname or not student.birth_date or not student.marks:
            print("!!! WRONG DATA !!!")
            print(f"Name: {student.name}, Surname: {student.surname}, Birth Date: {student.birth_date}, Marks: {student.marks}")


students = []
try:
    students = read_from_file("info_students.json")
    if len(students) == 0:
        raise PermissionError
except PermissionError:
    print("No students in list")
    quit()
except FileNotFoundError:
    print("File not found!")
    quit()

for student in students:
    if student.check_if_passed_exam():
        print(student)

check_correct_data(students)
