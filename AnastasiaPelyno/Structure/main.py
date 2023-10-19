class Student:
    def __init__(self, name, surname, birthday, grades):
        self.name = name
        self.surname = surname
        self.birthday = birthday
        self.grades = grades

    def passed_session(self):
        return all(grade >=51 for grade in self.grades)

def reading_students(file_name):
    students = []
    try:
        with (open(file_name, 'r') as file):
            lines = file.readlines()
            if len(lines)==0:
                raise ValueError
            for line in lines:
                information = line.strip().split()
                if len(information)== 4:
                    name=information[0]
                    surname=information[1]
                    birthday=information[2]
                    grades=information[3].split(',')
                    grades = [int(grade) for grade in grades]
                    student = Student(name, surname, birthday, grades)
                    students.append(student)
    except FileNotFoundError:
        print(f"File {file_name} not exist")
    except ValueError:
        print(f"File {file_name} is empty")
        exit(-1)
    return students

def students_not_passed_session(students):
    talon_students = []
    for student in students:
        if not student.passed_session():
            talon_students.append(student)
    return talon_students

students = reading_students('students.txt')
talon=students_not_passed_session(students)
for student in talon:
    print(f"NAME: {student.name}, SURNAME: {student.surname},BIRTHDAY: {student.birthday},GRADES: {student.grades}")
if len(talon)==0:
    print("All student successfully passed session")

