class Student:
    def __init__(self, first_name, last_name, birth_date, grades):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date
        self.grades = grades
def read_students_from_file(file_path):
    students = []
    try:
        with open(file_path, 'r') as file:
            for line in file:
                data = line.strip().split(',')
                first_name, last_name, birth_date, grades = data
                grades = [int(grade) for grade in grades.split()]
                student = Student(first_name, last_name, birth_date, grades, )
                students.append(student)
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except ValueError:
        print(f"Error: Invalid data format in the file '{file_path}'.")
    return students
def students_not_passing_exams(students):
    if not students:
        print("No student data found.")
        return
    all_passed = all(sum(student.grades) / len(student.grades) >= 51 for student in students)

    if all_passed:
        print("All students have passed the exams.")
    else:
        for student in students:
            average_grade = sum(student.grades) / len(student.grades)
            if average_grade < 51:
                print(f"{student.first_name} {student.last_name} did not pass exams.")

file_path = 'students.txt'
all_students = read_students_from_file(file_path)
students_not_passing_exams(all_students)
