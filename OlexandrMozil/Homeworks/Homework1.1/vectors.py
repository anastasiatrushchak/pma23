import numpy as np
class Vector:
    def __init__(self):
        self.vector = np.zeros(5, dtype=int)
        for i in range (0,5):
            self.vector[i] = int(input("Enter the number from vector: "))
    def __str__(self):
        return str(self.vector)
    def addition(self, other):
        print("Vectors addition:\n", np.add(self.vector, other.vector))
    def subtraction(self, other):
        print("Vectors subtraction:\n", np.subtract(self.vector, other.vector))
    def multiplication (self, other):
        print("Vectors multiplication:\n", np.multiply(self.vector, other.vector))
    def division (self, other):
        print("Vectors division:\n", np.divide(self.vector, other.vector))

vectorA = Vector()
print("Vector A is: ", vectorA, "\n")
vectorB = Vector()
print("Vector B is: ", vectorB, "\n")

vectorA.addition(vectorB)
vectorA.subtraction(vectorB)
vectorA.multiplication(vectorB)
vectorA.division(vectorB)