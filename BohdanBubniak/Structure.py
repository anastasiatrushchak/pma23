class Student:
    def __init__(self, name, surname, dob, grades):
        self.name = name
        self.surname = surname
        self.dob = dob
        self.grades = grades

    def __str__(self):
        return f"{self.name} {self.surname}, DOB: {self.dob}, Grades: {self.grades}"

def read_students_from_file(file_path):
    students = []
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            for i in range(0, len(lines), 4):
                first_name = lines[i].strip()
                last_name = lines[i+1].strip()
                birthdate = lines[i+2].strip()
                grades = [int(grade) for grade in lines[i+3].strip().split(',')]
                student = Student(first_name, last_name, birthdate, grades)
                students.append(student)
    except (FileNotFoundError, ValueError) as e:
        print(f"Помилка при читанні файлу: {e}")
    return students

def student_failed_session(students):
    failed_students = 0
    for student in students:
        if any(grade < 51 for grade in student.grades):
            print(student)
            failed_students += 1

    if failed_students == 0:
        print("Всі студенти склали сесію.")

students = read_students_from_file('students.txt')
student_failed_session(students)
