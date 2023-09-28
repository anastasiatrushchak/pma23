import constants
import os

matrix_a = []
matrix_b = []


class FileIsEmpty(Exception):

    def __init__(self, message="File is empty!"):
        self.message = message
        super().__init__(self.message)


class DetIsZero(Exception):

    def __init__(self, message="Can't transpose matrix if determinant is zero!"):
        self.message = message
        super().__init__(self.message)


try:
    with open(constants.INPUT_FILE, 'r') as file:
        if os.path.getsize(constants.INPUT_FILE) == 0:
            raise FileIsEmpty
        new_matrix = False
        lines = file.readlines()
        for line in lines:
            if line == '\n':
                new_matrix = True
                continue
            if new_matrix:
                elements = line.strip().split(constants.SEPARATOR)
                row = [float(element) for element in elements]
                matrix_b.append(row)
            else:
                elements = line.strip().split(constants.SEPARATOR)
                row = [float(element) for element in elements]
                matrix_a.append(row)
except FileNotFoundError as e:
    print("File not found!")

print(matrix_a)
print(matrix_b)


class Matrix:

    def __init__(self, matrix):
        self.matrix = matrix

    def __add__(self, matrix_b):
        result = []
        for i in range(len(matrix_b)):
            result.append([])
            for j in range(len(matrix_b[0])):
                result[i].append(self.matrix[i][j] + matrix_b[i][j])
        return result

    def __sub__(self, matrix_b):
        result = []
        for i in range(len(matrix_b)):
            result.append([])
            for j in range(len(matrix_b[0])):
                result[i].append(self.matrix[i][j] - matrix_b[i][j])
        return result

    def __mul__(self, matrix_b):
        result = []
        for i in range(len(matrix_b)):
            result.append([])
            for j in range(len(matrix_b[0])):
                result[i].append(0)
                for k in range(len(matrix_b)):
                    result[i][j] += self.matrix[i][k] * matrix_b[k][j]
        return result

    def __truediv__(self, matrix_b):
        det = self.determinant(matrix_b)
        try:
            if det == 0:
                raise DetIsZero
            else:
                transposed = []
                for i in range(len(matrix_b)):
                    transposed.append([])
                    for j in range(len(matrix_b[0])):
                        transposed[i].append(self.cofactor(matrix_b, i, j))
                transposed = self.transpose(transposed)

                inverse = []
                for i in range(len(transposed)):
                    inverse.append([])
                    for j in range(len(transposed[0])):
                        inverse[i].append(float(transposed[i][j]) / det)

                result = self * inverse
                return result
        except DetIsZero as e:
            print("Det can't be zero!")
            return 0

    def determinant(self, matrix):
        det = 0
        for i in range(len(matrix)):
            add = 1
            sub = 1
            for j in range(len(matrix)):
                add *= matrix[j][(i + j) % len(matrix)]
                sub *= matrix[j][(i - j) % len(matrix)]
            det += (add - sub)
        return det

    def transpose(self, matrix):
        rows = len(matrix)
        cols = len(matrix[0])
        result = [[None] * rows for _ in range(cols)]
        for i in range(rows):
            for j in range(cols):
                result[j][i] = matrix[i][j]
        return result

    def cofactor(self, matrix, row, col):
        addition = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i != row and j != col:
                    addition.append(matrix[i][j])
        result = ((-1) ** (row + col)) * (addition[0] * addition[3] - addition[2] * addition[1])
        return result


matrix_a = Matrix(matrix_a)

try:
    with open(constants.OUTPUT_FILE, 'w') as file:
        file.write("Addition:\n" + str(matrix_a + matrix_b) + '\n')
        file.write("Subtraction:\n" + str(matrix_a - matrix_b) + '\n')
        file.write("Multiplication:\n" + str(matrix_a * matrix_b) + '\n')
        file.write("Division:\n" + str(matrix_a / matrix_b) + '\n')

except FileNotFoundError:
    print("File not found!")
