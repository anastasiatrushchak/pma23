import abc

class School(metaclass=abc.ABCMeta):
    def daily_routine(self):
        self.enter_school()
        self.attend_classes()
        self.leave_school()

    def enter_school(self):
        pass

    def attend_classes(self):
        pass

    def leave_school(self):
        pass


class Student(School):
    def enter_school(self):
        print("Student enters the school")

    def attend_classes(self):
        print("Student attends classes")

    def leave_school(self):
        print("Student leaves the school")


class Teacher(School):
    def enter_school(self):
        print("Teacher enters the school")

    def attend_classes(self):
        print("Teacher teaches classes")

    def leave_school(self):
        print("Teacher leaves the school")


if __name__ == "main":
    student = Student()
    teacher = Teacher()

    print("Student's Daily Routine:")
    student.daily_routine()

    print("\nTeacher's Daily Routine:")
    teacher.daily_routine()
