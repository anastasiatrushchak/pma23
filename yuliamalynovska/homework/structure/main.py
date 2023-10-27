from student import Student


def read_students(file_name):
    students = []
    try:
        with open(file_name, 'r') as file:
            amount = int(file.readline().replace('\n', ''))
            for i in range(abs(amount)):
                name = file.readline().replace('\n', '')
                surname = file.readline().replace('\n', '')
                date_birth = file.readline().replace('\n', '')
                marks = [abs(int(mark)) for mark in file.readline().replace('\n', '').split()]
                students.append(Student(name, surname, date_birth, marks))
    except FileNotFoundError:
        print("No such file or directory")
    return students


def print_loosers(students):
    for student in students:
        for mark in student.marks:
            if mark < 51:
                print(student)
                break


students = read_students('info.txt')
print_loosers(students)


