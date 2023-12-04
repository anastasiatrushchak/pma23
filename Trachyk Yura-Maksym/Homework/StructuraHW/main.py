STUDENTS_FILE = "Students.txt"
separate = ','
class Student:
    def __init__(self, first_name, last_name, birth_date, grades):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date
        self.grades = grades

    def made_a_session(self):
        for grade in self.grades:
            if grade < 51:
                return False
        return True

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.birth_date}"

def read_students(file_name):

    try:
        students = []
        with open(file_name, 'r') as file:
            lines = file.readlines()
            if not lines:
                raise ValueError("The file is empty")
            for line in lines:
                data = line.split(separate)
                first_name = data[0]
                last_name = data[1]
                birth_date = data[2]
                grades = data[3:]
                grades = [int(grade) for grade in grades]
                student = Student(first_name, last_name, birth_date, grades)
                students.append(student)
        return students
    except FileNotFoundError:
        print("File not found")
        exit(-1)
    except ValueError as e:
        print(f"Error: {e}")
        exit(-1)

students = read_students(STUDENTS_FILE)
failed_students = []

for student in students:
    if not student.made_a_session():
        failed_students.append(student)

if failed_students:
    print("Students who did not pass the session:")
    for student in failed_students:
        print(student)
else:
    print("All students passed the session.")