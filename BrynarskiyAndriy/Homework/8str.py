from datetime import datetime

# Структура для опису студента
class Student:
    def __init__(self, first_name, last_name, birth_date, grades):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date
        self.grades = grades

    def calculate_average_grade(self):
        return sum(self.grades) / len(self.grades) if len(self.grades) > 0 else 0

    def has_passed_session(self, passing_grade=60):
        return self.calculate_average_grade() >= passing_grade

def read_students_from_file(file_path):
    students = []
    try:
        with open(file_path, 'r') as file:
            for line in file:
                student_data = line.strip().split(',')
                first_name, last_name = student_data[:2]
                birth_date = datetime.strptime(student_data[2], '%Y-%m-%d')
                grades = [int(grade) for grade in student_data[3:]]
                student = Student(first_name, last_name, birth_date, grades)
                students.append(student)
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except Exception as e:
        print(f"Error reading file: {e}")
    
    return students

def print_failed_students(students):
    print("Students who failed the session:")
    for student in students:
        if not student.has_passed_session():
            print(f"{student.first_name} {student.last_name} (Average Grade: {student.calculate_average_grade()})")

# Приклад використання
file_path = 'students_data.txt'  # Припустимо, що у вас є файл students_data.txt
students = read_students_from_file(file_path)
print_failed_students(students)