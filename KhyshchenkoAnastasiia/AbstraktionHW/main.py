# -*- coding: utf-8 -*-

class Student:
    def __init__(self, name, surname, date_of_birth, python_grades):
        self.name = name
        self.surname = surname
        self.date_of_birth = date_of_birth
        self.python_grades = python_grades

def read_students_from_file(file_path):
    students = []
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            data = line.strip().split(',')
            name, surname, date_of_birth, python_grades = data
            python_grades = [int(grade) for grade in python_grades.split()]
            student = Student(name, surname, date_of_birth, python_grades)
            students.append(student)
    return students

def did_not_pass_exams(student):
    has_failed = False
    for grade in student.python_grades:
        if grade == 2:
            has_failed = True
            break
    return has_failed or sum(student.python_grades) / len(student.python_grades) < 3

file_path = 'students.txt'  # Шлях до файлу з даними студентів.

# Зчитуємо студентів з файлу
students = read_students_from_file(file_path)

# Перевірка, чи всі студенти склали сесію
all_passed = all(not did_not_pass_exams(student) for student in students)

# Виводимо студентів, які не склали сесію
for student in students:
    if did_not_pass_exams(student):
        print(f"{student.name} {student.surname} не склав сесію. Середній бал: {sum(student.python_grades) / len(student.python_grades):.2f}")

# Вивід повідомлення про те, що всі студенти склали сесію
if all_passed:
    print("Вітаю! Всі студенти склали сесію!")
