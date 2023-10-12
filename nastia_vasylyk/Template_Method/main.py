from abc import ABC, abstractmethod

class SchoolSubject(ABC):

    def study_subject(self): # шаблонний метод класу і 3 абстрактні методи
        self.learn_material()
        self.take_tests()
        self.take_exam()

    @abstractmethod
    def learn_material(self):
        pass

    @abstractmethod
    def take_tests(self):
        pass

    @abstractmethod
    def take_exam(self):
        pass

class MathSubject(SchoolSubject):

    def learn_material(self):
        print("Studying Math material.")

    def take_tests(self):
        print("Taking Math tests.")

    def take_exam(self):
        print("Taking Math exam.")
# викликаємо метод
def main():
    math_subject = MathSubject()

    print("Math Subject:")
    math_subject.study_subject()


if __name__ == "__main__":
    main()

