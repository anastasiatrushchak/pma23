import json

class Student:
    def __init__(self, first_name, last_name, birthdate, grades):
        self.first_name = first_name
        self.last_name = last_name
        self.birthdate = birthdate
        self.grades = grades

    def __str__(self):
        return (
            f"Name: {self.first_name} {self.last_name}\n"
            f"Birth date: {self.birthdate}\n"
            f"Marks: {self.grades}\n"
        )


def read_students_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return []
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON format in '{file_path}'.")
        return []

    student_data = data.get("students", [])
    students = []

    for s_data in student_data:
        student = Student(
            s_data.get("First Name", ""),
            s_data.get("Last Name", ""),
            s_data.get("Date of Birth", ""),
            s_data.get("Grades", [])
        )
        students.append(student)

    return students

def students_who_failed(students):
    failed_students = []
    for student in students:
        if any(grade < 51 for grade in student.grades):
            failed_students.append(student)
    return failed_students


students = read_students_from_file("data.json")

if not students:
    print("No valid student data to process.")
else:
    for student in students:
        print(student)
    failed_students = students_who_failed(students)

    if len(failed_students) == 0:
        print("All students passed their exams!")
    else:
        print("Students who failed:")
        for student in failed_students:
            print(f"{student.first_name} {student.last_name}")


