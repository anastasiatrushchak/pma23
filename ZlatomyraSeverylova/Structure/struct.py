STUDENTS = 'students.txt'
FILE_NOT_FOUND_ERROR = 'No such file or directory'
'''from collections import namedtuple'''
'''from typing import NamedTuple'''

class Students():
    def __init__(self, name, surname, data_of_birth, grades):
        self.name = name
        self.surname = surname
        self.data_of_birth = data_of_birth
        self.grades = sum(grades)

    '''def __str__(self):
        return f'{self.name} {self.surname} birthday: {self.data_of_birth} grades: {self.grades}'''

'''class Students(NamedTuple):
    name: str
    surname: str
    data_of_birth: str
    grades: list'''
students = []
def read(path):
     try:
        with open(path, 'r') as file:
            for l in file:
                st = l.split()
                name = st[0]
                surname = st[1]
                data_of_birth = st[2]
                grades = [int(gr) for gr in st[3:]]
                students.append(Students(name, surname, data_of_birth, grades))
            return students
     except FileNotFoundError:
        print(FILE_NOT_FOUND_ERROR)
        exit(-1)

def check_grades(students):
    for student in students:
        if student.grades < 51:
            print(f"{student.name} {student.surname} did not complete the session")
        else:
            print(f"{student.name} {student.surname} completed the session")


stud = read(STUDENTS)
check_grades(stud)


