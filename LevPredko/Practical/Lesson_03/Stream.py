from pyxtension.streams import stream
class Employee:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
    def print(self):
        return f"Name: {self.name} ; Surname: {self.surname}\n"

employee1 = Employee('Oleh', 'Stepanyak')
employee2 = Employee('Dima', 'Vasilision')
employee3 = Employee('Lev', 'Predko')

employee = []
employee.append(employee1)
employee.append(employee2)
employee.append(employee3)

change_employee = (stream(employee)
                   .map(lambda l: l.print() + "Andriy Oliynik")
                   .filter()
                   .toList())
print(change_employee[0], change_employee[1], change_employee[2])