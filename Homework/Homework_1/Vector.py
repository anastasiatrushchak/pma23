import numpy as np
class Vector:
    def __init__(self, vector):
        self.vector = vector
        self.size = vector.size
    @classmethod
    def random(cls,size):
        vector = np.random.randint(1, 11, size = size)
        return cls(vector)
    @classmethod
    def from_file(cls, file_name):
        vector = np.loadtxt(file_name, dtype=int,delimiter=" ")
        return cls(vector)
    def __str__(self):
        return self.vector.__str__();
    def append(self, new_element):
        self.vector.append(new_element)
    def __add__(self, other):
        return  self.vector + other
    def __sub__(self, other):
        return  self.vector - other
    def __mul__(self, other):
        return self.vector * other
    def __truediv__(self, other):
        return self.vector / other