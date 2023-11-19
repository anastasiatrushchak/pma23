class Student:
    def __init__(self, name, surname, grades: list, birthday: list):
        self.__err_handler(name, surname, grades, birthday)
        self.name = name
        self.surname = surname
        self.grades = grades
        self. birthday = birthday

    @staticmethod
    def __err_handler(name, surname, grades, birthday):
        grades = [int(i) for i in grades]
        birthday = [int(i) for i in birthday]
        if name == "" or surname == "":
            raise ValueError("Error! NAME or SURNAME doesn't exist!")
        if not len(grades) == 3 or not len(birthday) == 3:
            raise ValueError("Error! Wrong size in GRADES or in BIRTHDAY!")
        for i in grades:
            if i > 100 or i < 0:
                raise ValueError("Error! Grade can't be more than 100 of less than 0")
        for i in birthday:
            if i < 0:
                raise ValueError("Error! date can't be less than 0!")
        if birthday[1] > 12:
            raise ValueError("Error! Month number can't be > 12!")
        if birthday[2] > 31:
            raise ValueError("Error! Day number can't be > 31!")

    def check_grades(self):
        grades = [int(i) for i in self.grades]
        for grade in grades:
            if grade < 51:
                return True
            else: return False

    def __str__(self):
        return "Student: " + self.surname + " " + self.name + "\nDate of birth: " + self.birthday[0] + '.' + self.birthday[1] + '.' +self.birthday[2]
