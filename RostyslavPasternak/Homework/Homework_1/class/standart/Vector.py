import random
from RostyslavPasternak.Homework.Homework_1.Exception import InvalidSize, InvalidType
class Vector:
    def __init__(self, vector):
        self.vector = vector
        self.size = len(vector)
    @classmethod
    def random(cls,size, a=1, b=9):
        vector = [random.randint(a, b) for _ in range(size)]

        return cls(vector)
    @classmethod
    def from_file(cls, file_name, separator=" "):
        with open(file_name, 'r') as readFile:
            line = readFile.readline()

        vector = line.split(separator)
        vector = [float(i) for i in vector if i.isdigit()]
        return cls(vector)
    def __str__(self):
        return self.vector.__str__()
    def str_to_file(self, file_name="result.txt"):
        with open(file_name, 'w') as writeFile:
            writeFile.write(str(self))
    def append(self, new_element):
        self.vector.append(new_element)
        self.size += 1
    def __add__(self, other):
        if isinstance(other, Vector):
            if self.size != other.size:
                raise InvalidSize()
            result = [self.vector[i] + other.vector[i] for i in range(self.size)]
            return Vector(result)
        elif isinstance(other, (int, float)):
            result = [self.vector[i] + other for i in range(self.size)]
            return Vector(result)
        raise InvalidType()

    def __sub__(self, other):
        if isinstance(other, Vector):
            if self.size != other.size:
                raise InvalidSize()
            result = [self.vector[i] - other.vector[i] for i in range(self.size)]
            return Vector(result)
        elif isinstance(other, (int, float)):
            result = [self.vector[i] - other for i in range(self.size)]
            return Vector(result)
        raise InvalidType()
    def __mul__(self, other):
        if isinstance(other, Vector):
            if self.size != other.size:
                raise InvalidSize()
            result = [self.vector[i] * other.vector[i] for i in range(self.size)]
            return Vector(result)
        elif isinstance(other, (int, float)):
            result = [self.vector[i] * other for i in range(self.size)]
            return Vector(result)
        raise InvalidType()
    def __truediv__(self, other):
        if isinstance(other, Vector):
            if self.size != other.size:
                raise InvalidSize()
            result = [self.vector[i] / other.vector[i] for i in range(self.size)]
            return Vector(result)
        elif isinstance(other, (int, float)):
            result = [self.vector[i] / other for i in range(self.size)]
            return Vector(result)
        raise InvalidType()