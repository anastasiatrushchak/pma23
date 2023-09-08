import numpy as np

class Matrix:
    def __init__(self, data):
        self.data = data
    @staticmethod
    def from_file(filename):
        try:
            with open(filename, 'r') as f:
                matrix = [[int(num) for num in line.split()] for line in f]
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

    def add(self, B):
        try:
            if self.data.shape != B.data.shape:
                raise ValueError("Matrix dimensions must be the same for addition.")
            return Matrix(np.add(self.data, B.data))
        except ValueError as e:
            return f"ValueError: {e}"

    def subtract(self, B):
        try:
            if self.data.shape != B.data.shape:
                raise ValueError("Matrix dimensions must be the same for subtraction.")
            return Matrix(np.subtract(self.data, B.data))
        except ValueError as e:
            return f"ValueError: {e}"

    def multiply(self, B):
        try:
            if self.data.shape[1] != B.data.shape[0]:
                raise ValueError("Number of columns in the first matrix must be equal to the number of rows in the second matrix for multiplication.")
            return Matrix(np.dot(self.data, B.data))
        except ValueError as e:
            return f"ValueError: {e}"

    def divide(self, B):
        try:
            if self.data.shape[1] != B.data.shape[0]:
                raise ValueError("Number of columns in the first matrix must be equal to the number of rows in the second matrix for division.")
            inverse_B = np.linalg.inv(B.data)
            return Matrix(np.dot(self.data, inverse_B))
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
    operation = input("Enter operation (add, subtract,multiplication, divide): ")
    if operation == 'add':
        result = MatrixA.add(MatrixB)
    elif operation == 'subtract':
        result = MatrixA.subtract(MatrixB)
    elif operation == 'multiply':
        result = MatrixA.multiply(MatrixB)
    elif operation == 'divide':
        result = MatrixA.divide(MatrixB)
    else:
        print("Invalid operation")

    if result is not None:
        print("The result is:")
        for row in result.data:
            print(' '.join(['{:0.5g}'.format(x) for x in row]))
        result.to_file('result_matrix.txt')
