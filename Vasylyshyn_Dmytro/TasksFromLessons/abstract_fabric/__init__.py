from abc import ABC, abstractmethod

class SchoolSubjectFactory(ABC):
    @abstractmethod
    def create_subject(self):
        pass

    @abstractmethod
    def create_teacher(self):
        pass

class MathFactory(SchoolSubjectFactory):
    def create_subject(self):
        return Math()

    def create_teacher(self):
        return MathTeacher()

class SchoolSubject(ABC):
    @abstractmethod
    def study(self):
        pass

class Teacher(ABC):
    @abstractmethod
    def teach(self):
        pass

class Math(SchoolSubject):
    def study(self):
        return "Studying Math"

class MathTeacher(Teacher):
    def teach(self):
        return "Teaching Math"

math_factory = MathFactory()
math_subject = math_factory.create_subject()
math_teacher = math_factory.create_teacher()

print(math_subject.study())
print(math_teacher.teach())

