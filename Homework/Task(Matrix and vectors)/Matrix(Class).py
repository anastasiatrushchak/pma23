import numpy as np

class Matrix:
    def __init__(self, data):
        self.data = data

    @staticmethod
    def from_file(filename):
        try:
            with open(filename, 'r') as f:
                matrix = [[float(num) for num in line.split()] for line in f]
            return Matrix(np.array(matrix))
        except FileNotFoundError:
            return f"File '{filename}' not found"
        except ValueError as e:
            return f"Error reading matrix from '{filename}': {e}"

    def to_file(self, filename):
        try:
            with open(filename, 'w') as f:
                for row in self.data:
                    f.write(' '.join(['{:0.5g}'.format(x) for x in row]) + '\n')
        except Exception as e:
            return f"Error writing matrix to '{filename}': {e}"

    @staticmethod
    def add(A, B):
        try:
            return Matrix(np.add(A.data, B.data))
        except ValueError as e:
            return f"ValueError: {e}"

    @staticmethod
    def subtract(A, B):
        try:
            return Matrix(np.subtract(A.data, B.data))
        except ValueError as e:
            return f"ValueError: {e}"

    @staticmethod
    def multiply(A, B):
        try:
            return Matrix(np.dot(A.data, B.data))
        except ValueError as e:
            return f"ValueError: {e}"

    @staticmethod
    def divide(A, B):
        try:
            inverse_B = np.linalg.inv(B.data)
            return Matrix(np.dot(A.data, inverse_B))
        except ValueError as e:
            return f"ValueError: {e}"
        except np.linalg.LinAlgError as e:
            return f"LinalgError: {e}"

MatrixA = Matrix.from_file('matrix_A.txt')
MatrixB = Matrix.from_file('matrix_B.txt')

if isinstance(MatrixA, str) or isinstance(MatrixB, str):
    print(MatrixA)
    print(MatrixB)
else:
    operation = input("Enter operation (add, subtract, multiply, divide): ")
    if operation == 'add':
        result = Matrix.add(MatrixA, MatrixB)
    elif operation == 'subtract':
        result = Matrix.subtract(MatrixA, MatrixB)
    elif operation == 'multiply':
        result = Matrix.multiply(MatrixA, MatrixB)
    elif operation == 'divide':
        result = Matrix.divide(MatrixA, MatrixB)
    else:
        result = "Invalid operation"

    print("The result is:")
    for row in result.data:
        print(' '.join(['{:0.5g}'.format(x) for x in row]))
    #print in file
    result.to_file('result_matrix.txt')

