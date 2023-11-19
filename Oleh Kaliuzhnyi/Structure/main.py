import json
from Student import Student

JSON_FILE = "Students.json"


def parse_json(filename, students):
    with open(filename) as file:
        json_list = json.load(file)
    for element in json_list:
        try:
            if not 'name' in element or not 'surname' in element or not 'grades' in element or not 'birth' in element:
                raise Exception("Error! Wrong data, some value doesn't exist in file!")
            student = Student(element['name'], element['surname'], element['grades'], element['birth'])
            students.append(student)
        except ValueError as val_err:
            print(val_err)


try:
    students = []
    parse_json(JSON_FILE, students)
    if len(students) == 0:
        raise Exception("Error! No students in list")
    for student in students:
        if student.check_grades():
            print("Didn't pass exams:")
            print(student)
except Exception as er:
    print(er)
