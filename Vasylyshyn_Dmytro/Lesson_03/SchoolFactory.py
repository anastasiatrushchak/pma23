class SchoolSubjectFactory(ABC):
    @abstractmethod
    def create_subject(self):
        pass

    @abstractmethod
    def create_teacher(self):
        pass