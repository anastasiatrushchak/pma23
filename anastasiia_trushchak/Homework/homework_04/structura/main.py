class Student:
    def __init__(self, last_name, first_name, birth_date, grades):
        self.last_name = last_name
        self.first_name = first_name
        self.birth_date = birth_date
        self.grades = grades

    def failed_session(self, passing_grade=3):
        if not self.grades:
            return True
        return any(grade < passing_grade for grade in self.grades)


def read_from_file(data_file):
    students = []
    try:
        with open(data_file, 'r') as file:
            for line_num, line in enumerate(file, start=1):
                student_data = line.strip().split(',')
                last_name, first_name = student_data[:2]
                birth_date = student_data[2]
                try:
                    grades = [int(grade) for grade in student_data[3:]]
                except ValueError:
                    raise ValueError(f"Non-numeric grade found in line {line_num}")
                if any(grade < 0 for grade in grades):
                    raise ValueError(f"Negative grade found in line {line_num}")
                student = Student(last_name, first_name, birth_date, grades)
                students.append(student)
    except FileNotFoundError:
        print("File not found.")
    return students



def print_failed(students):
    failed_students = [student for student in students if student.failed_session(passing_grade=3)]
    if not failed_students:
        print("Немає таких студентів, які не склали сесію.")
    else:
        print("Students who failed the session:")
        for student in failed_students:
            print(f"{student.last_name} {student.first_name}")


data_file = 'output.txt'
try:
    students = read_from_file(data_file)
    print_failed(students)
except ValueError as e:
    print(f"An error occurred: {str(e)}")

