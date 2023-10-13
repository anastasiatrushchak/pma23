import json
class Student:
    def __init__(self, firstname, surname, date, list_of_grades):
        self.firstname = firstname
        self.surname = surname
        self.date = date
        self.list_of_grades = list_of_grades
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
    s = Student.fromJson(new_element)
    list.append(Student.fromJson(new_element))
print("<--------------------All Student-------------------->")
for s in list:
    print(s)
print("<--------------------Not pass-------------------->")
for s in list:
    if not s.is_exam_passed():
        print(s)