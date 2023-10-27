
class Student:
    def __init__(self, name, surname, date_birth, marks):
        self.name = name
        self.surname = surname
        self.date_birth = date_birth
        self.marks = marks

    def __str__(self):
        return f"Name: {self.name} \nSurname: {self.surname} \nDate of birth: {self.date_birth} \nMarks: {self.marks}"
