class Student:
    def __init__(self, f_name, l_name, b_date, grades=None):
        self.firstname = f_name
        self.lastname = l_name
        self.birthdate = b_date
        if grades is not None:
            self.grades = [int(grade) for grade in grades]

    def final_grade(self):
        if hasattr(self, 'grades'):
            return sum(self.grades)
        else:
            return 0

    def print_info(self):
        print(f'First name: {self.firstname}')
        print(f'Last name: {self.lastname}')
        print(f'Date of birth: {self.birthdate}')
        print(f'Final grade: {self.final_grade()}')


try:
    with open("input.txt", "r") as in_f:
        students = []
        for line in in_f:
            student = line.split()
            if len(student) < 3:
                print(f"Error: Invalid data format in line: {line}")
                continue

            f_name = student[0]
            l_name = student[1]
            b_date = student[2]
            grades = []
            for i in range(3, len(student)):
                try:
                    grades.append(int(student[i]))
                except ValueError:
                    print(f"Error: Invalid grade in line: {line}")
            students.append(Student(f_name, l_name, b_date, grades))

    for student in students:
        if student.final_grade() <= 50:
            student.print_info()
except FileNotFoundError:
    print("Error: The file 'input.txt' does not exist.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")