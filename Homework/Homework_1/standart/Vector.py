import random
class Vector:
    def __init__(self, vector):
        self.vector = vector
        self.size = len(vector)
    @classmethod
    def random(cls,size, a=1, b=9):
        vector = [random.randint(a, b) for _ in range(size)]

        return cls(vector)
    @classmethod
    def from_file(cls, file_name):
        with open(file_name, 'r') as readFile:
            line = readFile.readline()

        vector = line.split(" ")
        return cls(vector)
    def __str__(self):
        return self.vector.__str__();
    def append(self, new_element):
        self.vector.append(new_element)
        self.size+=1
    def __add__(self, other):
        if isinstance(other, Vector):
            if self.size == other.size:
                result = [self.vector[i] + other.vector for i in range(self.size)]
                return Vector(result)
        elif isinstance(other, (int, float)):
            result = [self.vector[i] + other for i in range(self.size)]
            return Vector(result)

    def __sub__(self, other):
        if isinstance(other, Vector):
            if self.size == other.size:
                result = [self.vector[i] - other.vector for i in range(self.size)]
                return Vector(result)
        elif isinstance(other, (int, float)):
            result = [self.vector[i] - other for i in range(self.size)]
            return Vector(result)
    def __mul__(self, other):
        if isinstance(other, Vector):
            if self.size == other.size:
                result = [self.vector[i] * other.vector for i in range(self.size)]
                return Vector(result)
        elif isinstance(other, (int, float)):
            result = [self.vector[i] * other for i in range(self.size)]
            return Vector(result)
    def __truediv__(self, other):
        if isinstance(other, Vector):
            if self.size == other.size:
                result = [self.vector[i] / other.vector for i in range(self.size)]
                return Vector(result)
        elif isinstance(other, (int, float)):
            result = [self.vector[i] / other for i in range(self.size)]
            return Vector(result)