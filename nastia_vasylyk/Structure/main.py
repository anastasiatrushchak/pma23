class Student:
    def __init__(self, name, surname, dob, marks):
        self.name = name
        self.surname = surname
        self.dob = dob
        self.marks = marks

    def __str__(self):# представляємо студента як стрінгу
        return f"Name: {self.name}, Surname: {self.surname}, Date of birth: {self.dob}, Marks: {self.marks}"


def read_students(filename):
    students = []
    try:
        with open(filename, 'r') as file:
            n = int(file.readline())
            for _ in range(n):
                name = file.readline().replace("\n", "")
                surname = file.readline().replace("\n", "")
                dob = file.readline().replace("\n", "")
                marks = [int(m) for m in file.readline().split()]
                students.append(Student(name, surname, dob, marks))
    except FileNotFoundError:
        print(-1)
    except Exception as e:
        print(e)
    return students


def fail_exam(students):
    temp = 0
    for student in students:
        for mark in student.marks:
            if mark < 51:
                print(student)
            else:
                temp += 1
    if temp > 0:
        print("All pass")


students = read_students("/Users/nasta/PycharmProjects/Structure/student.txt")
fail_exam(students)
# for s in students:
#     print (s)