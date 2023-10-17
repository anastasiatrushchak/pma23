import json
import re

class InvalidData(Exception):
    def __init__(self):
        super().__init__("InvalidData")
def validate_string_format(input_string):
    pattern = r"^\d{4}-\d{2}-\d{2}$"

    if re.match(pattern, input_string):
        return False
    else:
        return True

class Student:
    def __init__(self, firstname, surname, date, list_of_grades):
        self.firstname = firstname
        self.surname = surname
        self.date = date
        self.list_of_grades = list_of_grades
        if len(self.firstname) == 0 or len(self.surname) == 0 or len(self.list_of_grades) == 0:
            raise InvalidData
        if validate_string_format(self.date):
            raise InvalidData


    @classmethod
    def fromJson(cls,json):
        firstname = json["Name"]
        surname = json["Surname"]
        date = json["Date_of_Birth"]
        list_of_grades = json["Grades"]
        return cls(firstname, surname, date, list_of_grades)
    def __str__(self):
        return (f"Name:{self.firstname} {self.surname}\n"
                f"Date of Birth: {self.date}\n"
                f"{self.list_of_grades}\n")
    def is_exam_passed(self):
        for score in self.list_of_grades:
            if score < 51:
                return False
        return True


with open('student.json', 'r') as file:
    all_student_json = json.load(file)

list = []
for new_element in all_student_json:
    try:
        s = Student.fromJson(new_element)
        list.append(Student.fromJson(new_element))
    except InvalidData as e:
        print(e)

print("<--------------------All Student-------------------->")
for s in list:
    print(s)
print("<--------------------Not pass-------------------->")
for s in list:
    if not s.is_exam_passed():
        print(s)