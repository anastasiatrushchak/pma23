class Student:
    def __init__(self, name, surname, age, grades):
        self.name = name
        self.surname = surname
        self.age = age
        self.grades = grades

    def fail(self):
        return any(grade < 3 for grade in self.grades)


def read_from_file(file):
    students = []
    with open(file, 'r') as f:
        for line in f:
            data = line.strip().split(' ')
            name = data[0]
            surname = data[1]
            age = data[2]
            grades = list(map(int, data[3].split(',')))
            student = Student(name, surname, age, grades)
            students.append(student)
    return students


def prints(students):
    for student in students:
        if student.fail():
            print(f"{student.name} {student.surname} з оцінками  {student.grades}  не склав іспити")


students = read_from_file("students.txt")
prints(students)
