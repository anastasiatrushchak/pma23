from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self, first_name, last_name, position):
        self.first_name = first_name
        self.last_name = last_name
        self.position = position
    def introduce(self):
        return f"Hello, I am {self.first_name} {self.last_name}, a {self.position}."

    @abstractmethod
    def work(self):
        pass

    def info(self):
        intro = self.introduce()
        work_result = self.work()
        return f"{intro} {work_result}"

class Manager(Person):


    def work(self):
        return "I'm managing the team and making important decisions."


class Employee(Person):


    def work(self):
        return "I'm doing my job as an employee."

manager = Manager("John", "Doe", "Manager")
employee = Employee("Alice", "Smith", "Employee")

print(manager.info())
print(employee.info())
