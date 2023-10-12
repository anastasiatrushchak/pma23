class Student:
    def __init__(self):
        self.name = ""
        self.surname = ""
        self.birth_date = ""
        self.marks = []

    def read_from_file(self, filename):
        with open(filename, "r") as readFile:
            self.name = readFile.readline().strip()
            self.surname = readFile.readline().strip()
            self.birth_date = readFile.readline().strip()
            self.marks = list(readFile.readline().strip().split(" "))

    def __str__(self):
        return (f"Name: {self.name} {self.surname}\n"
                f"Birth date: {self.birth_date}\n"
                f"Marks: {self.marks}\n")


student = Student()
student.read_from_file("info_students.txt")
print(student)

