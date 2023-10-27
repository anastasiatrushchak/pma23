import os
def file_exists(filename):
    if os.path.isfile(filename):
        print("Файл існує.")
        with open(filename, 'r') as file:
            if file.read() == "":
                print("Файл порожній.")
            else:
                print("Файл не порожній.")
    else:
        print("Файл не існує.")

file_exists("fileS.txt")

class Student:
    def __init__(self, first_name, last_name, birthdate, grades):
        self.first_name = first_name
        self.last_name = last_name
        self.birthdate = birthdate
        self.grades = grades

def read_students_from_file(file_path):
    students = []
    with open(file_path, 'r') as file:
        for line in file:
            data = line.strip().split(',')
            first_name, last_name, birthdate, grades = data[0], data[1], data[2], [int(grade) for grade in data[3:]]
            student = Student(first_name, last_name, birthdate, grades)
            students.append(student)
    return students

def students_failed_exams(students):
    for student in students:
        average_grade = sum(student.grades) / len(student.grades)
        if average_grade < 60:
            print(f"{student.first_name} {student.last_name} failed with an average grade of {average_grade:.2f}")

file_path = "fileS.txt"
students = read_students_from_file(file_path)
students_failed_exams(students)