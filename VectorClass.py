import numpy as np

class VectorOperations:
    def __init__(self, vector1, vector2, skalar):
        self.vector1 = vector1
        self.vector2 = vector2
        self.skalar = skalar

    def add(self):
        result = self.vector1 + self.vector2
        print("add:", result)

    def sub(self):
        result1 = self.vector1 - self.vector2
        print("sub:", result1)

    def dot(self):
        result2 = np.dot(self.vector1, self.vector2)  # скалярний добуток
        print("SkalarMult:", result2)

    def cross(self):
        result3 = np.cross(self.vector1, self.vector2)  # векторний добуток
        print("VectorMult:", result3)

    def scalar_multiply(self):
        result4 = self.vector1 * self.skalar
        print("MultBySkalar:", result4)

    def vector_division(self):
        result5 = self.vector1 / self.vector2
        print("Division:", result5)

    def scalar_division(self):
        result6 = self.vector1 / self.skalar
        print("DivisionByScalar:", result6)

vector1 = np.array([1, 2, 3])
vector2 = np.array([4, 5, 6])
skalar = 2

vector_operations = VectorOperations(vector1, vector2, skalar)

operation = input()
if operation == "add":
    vector_operations.add()
if operation == "sub":
    vector_operations.sub()
if operation == "dot":
    vector_operations.dot()
if operation == "cross":
    vector_operations.cross()
if operation == "MultBySalar":
    vector_operations.scalar_multiply()
if operation == "Division":
    vector_operations.vector_division()
if operation == "DivisionBySkalar":
    vector_operations.scalar_division()
