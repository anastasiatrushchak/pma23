class Student:
    def __init__(self, first_name, last_name, birth_date, grades):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date
        self.grades = grades

    def has_failed(self):
        return any(grade < 3 for grade in self.grades)

def read_students_from_file(file_path):
    students = []
    with open(file_path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            data = line.strip().split(' ')
            first_name = data[0]
            last_name = data[1]
            birth_date = data[2]
            grades = list(map(int, data[3].split(',')))
            student = Student(first_name, last_name, birth_date, grades)
            students.append(student)
    return students

def print_students_who_failed(students):
    for student in students:
        if student.has_failed():
            print(f"Студент {student.first_name} {student.last_name} не склав сесію.")

students = read_students_from_file('students.txt')
print_students_who_failed(students)
