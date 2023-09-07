import numpy as np


class Matrix:
    def __init__(self, filename):
        self.filename = filename
        self.vectorA, self.vectorB = self.read_vectors()

    def read_vectors(self):
        try:
            with open(self.filename, 'r') as f:
                vectorA = np.array([float(num) for num in f.readline().split(',')])
                vectorB = np.array([float(num) for num in f.readline().split(',')])
            return vectorA, vectorB
        except Exception as e:
            print(f"Error reading vectors from file: {e}")
            return None, None

    def write_vector(self, filename, vector):
        try:
            with open(filename, 'w') as f:
                f.write(', '.join(['{:0.5g}'.format(x) for x in vector]) + '\n')
        except Exception as e:
            print(f"Error writing vector to file: {e}")

    def vector_add(self):
        return self.vectorA + self.vectorB

    def vector_subtract(self):
        return self.vectorA - self.vectorB

    def vector_multiply(self):
        return self.vectorA * self.vectorB

    def vector_divide(self):
        try:
            return self.vectorA / self.vectorB
        except ZeroDivisionError:
            print("Error: Division by zero is not allowed.")
            return None


matrix = Matrix('vectors.txt')
if matrix.vectorA is None or matrix.vectorB is None:
    print("Exiting due to error.")
else:
    operation = input("Enter operation (add, subtract, multiply, divide): ")
    if operation == 'add':
        result = matrix.vector_add()
    elif operation == 'subtract':
        result = matrix.vector_subtract()
    elif operation == 'multiply':
        result = matrix.vector_multiply()
    elif operation == 'divide':
        result = matrix.vector_divide()
        if result is None:
            print("Exiting due to error.")
    else:
        print("Invalid operation")

    if result is not None:
        print(', '.join('{:0.5g}'.format(x) for x in result))
        matrix.write_vector('result_vector.txt', result)
