import numpy as np


class Matrix:
    def __init__(self):
        self.matrix = 0
        a = int(input('size of matrix:'))
        self.matrix = np.random.randint(0, 11, (a, a))

    def __str__(self):
        return str(self.matrix)

    def add(self, other):
        print("Addition of matrices:\n", np.add(self.matrix, other.matrix))

    def sub(self, other):
        print("Subtraction of matrices:\n", np.subtract(self.matrix, other.matrix))

    def mult(self, other):
        print("Multiplication of matrices:\n", np.matmul(self.matrix, other.matrix))

    def division(self, other):
        print("Division of matrices:\n", self.matrix @ np.linalg.inv(other.matrix))


class Vector:
    def __init__(self):
        self.vector = 0
        a = int(input('size 1 vector:'))
        self.vector = np.random.randint(0, 11, (a))
    def __str__(self):
        return str(self.vector)
    def add(self, other):
        print("Addition of vectors:\n", np.add(self.vector, other.vector))
    def sub(self, other):
        print("Subtraction of vectors:\n", np.subtract(self.vector, other.vector))
    def mult (self, other):
        print("Multiplication of vectors:\n", np.multiply(self.vector, other.vector))
    def division (self, other):
        print("Division of vectors:\n", np.divide(self.vector, other.vector))
choice = input("Matrix or Vector? (M or V):")
if choice =="M":
    matrixA = Matrix()
    print(matrixA)
    matrixB = Matrix()
    print(matrixB)
    operation = input("operation:")
    if operation == "+":
        matrixA.add(matrixB)
    elif operation == "-":
        matrixA.sub(matrixB)
    elif operation == "*":
        matrixA.mult(matrixB)
    elif operation == "/":
        matrixA.division(matrixB)
elif choice == "V":
    vectorA = Vector()
    print("Vector A is: ", vectorA, "\n")
    vectorB = Vector()
    print("Vector B is: ", vectorB, "\n")
    operation = input("operation:")
    if operation == "+":
        vectorA.add(vectorB)
    elif operation == "-":
        vectorA.sub(vectorB)
    elif operation == "*":
        vectorA.mult(vectorB)
    elif operation == "/":
        vectorA.division(vectorB)



