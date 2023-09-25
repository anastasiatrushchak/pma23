class Vector:
    def __init__(self, first_vector, second_vector):
        self.first_vector = first_vector
        self.second_vector = second_vector
    def __add__(self,other):
        return[a + b for a, b in zip(self.first_vector, other.second_vector)]
    def __sub__(self, other):
        return [a - b for a, b in zip(self.first_vector, other.second_vector)]
    def __mul__(self, other):
        return[a * b for a, b in zip(self.first_vector, other.second_vector)]
    def __truediv__(self, other):
        return [a / b for a, b in zip(self.first_vector,other.second_vector)]