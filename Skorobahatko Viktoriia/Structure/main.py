class Student:
    def __init__(self, name, lastName, dateOfBirth, marks):
        self.name = name
        self.lastName = lastName
        self.dateOfBirth = dateOfBirth
        self.marks = marks

    @staticmethod
    def read_students(input_file):
        students = []
        try:
           with open(input_file, 'r') as file:
               for line in file:
                   parts = line.strip().split()
                   if len(parts) != 6:
                       raise ValueError("Invalid data in the input file")
                   name = parts[0]
                   lastName = parts[1]
                   dateOfBirth = parts[2]
                   marks = list(map(int, parts[3:]))
                   student = Student(name, lastName, dateOfBirth, marks)
                   students.append(student)
           return students
        except FileNotFoundError:
            print("File not found")
        except ValueError as e:
            print(f"Error processing: {str(e)}")

    @staticmethod
    def write():
        print(f"{student.name} {student.lastName}, Date of Birth: {student.dateOfBirth}, Marks: {student.marks}")
    @staticmethod
    def session(students):
        small_marked_students = []
        for student in students:
            if any(mark < 51 for mark in student.marks):
                small_marked_students.append(student)
        return small_marked_students


students = Student.read_students("input.txt")
if students:
    small_marked_students = Student.session(students)
    if small_marked_students:
        print("Students who did not pass the session:")
        for student in small_marked_students:
            student.write()
    else:
        print("All students passed the session successfully.")
else:
    print("No valid student data found in the input file.")
