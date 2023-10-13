STUDENT_FILE = "students.txt"


class Student:
    def __init__(self, first_name, last_name, birth_date, grades):
        self.first_name, self.last_name, self.birth_date, self.grades = first_name, last_name, birth_date, grades

    def __str__(self):
        return f"Ім'я: {self.first_name}, Прізвище: {self.last_name}, Дата народження: {self.birth_date}, Оцінки: {', '.join(map(str, self.grades))}"


def read_students_from_file(file_path):
    students = []

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                data = line.strip().split(';')
                if len(data) == 4:
                    first_name, last_name, birth_date, grades_data = data
                    birth_date = birth_date.strip()
                    grades = [int(grade) for grade in grades_data.split(',')]
                    students.append(Student(first_name, last_name, birth_date, grades))
                else:
                    print(f"Неправильний формат рядка: {line}")

    except FileNotFoundError:
        print(f"Файл '{file_path}' не знайдено.")

    return students


def find_students_who_failed(students):
    return [student for student in students if all(grade < 51 for grade in student.grades)]


def main():
    students = read_students_from_file(STUDENT_FILE)

    if not students:
        print("Немає даних про студентів.")
        return

    failed_students = find_students_who_failed(students)

    if not failed_students:
        print("Всі студенти склали сесію!")
    else:
        print("Студенти, які не склали сесію:")
        for student in failed_students:
            print(student)

if __name__ == "__main__":
    main()

