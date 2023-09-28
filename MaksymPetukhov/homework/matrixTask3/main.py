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
    print(e)


def add(matrix_a, matrix_b):
    result = []
    for i in range(len(matrix_a)):
        result.append([])
        for j in range(len(matrix_a[0])):
            result[i].append(matrix_a[i][j] + matrix_b[i][j])
    with open(constants.OUTPUT_FILE, 'w') as file:
        file.write(str(result))
    return result


def subtract(matrix_a, matrix_b):
    result = []
    for i in range(len(matrix_a)):
        result.append([])
        for j in range(len(matrix_a[0])):
            result[i].append(matrix_a[i][j] - matrix_b[i][j])
    with open(constants.OUTPUT_FILE, 'w') as file:
        file.write(str(result))
    return result


def multiply(matrix_a, matrix_b):
    result = []

    for i in range(len(matrix_a)):
        result.append([])
        for j in range(len(matrix_a[0])):
            result[i].append(0)
            for k in range(len(matrix_b)):
                result[i][j] += matrix_a[i][k] * matrix_b[k][j]

    with open(constants.OUTPUT_FILE, 'w') as file:
        file.write(str(result))

    return result


def divide(matrix_a, matrix_b):
    det = determinant(matrix_b)

    if det == 0:
        raise DetIsZero

    transposed = []
    for i in range(len(matrix_a)):
        transposed.append([])
        for j in range(len(matrix_a[0])):
            transposed[i].append(cofactor(matrix_b, i, j))
    print(transposed)
    transposed = transpose(transposed)
    print(transposed)

    inverse = []
    for i in range(len(transposed)):
        inverse.append([])
        for j in range(len(transposed[0])):
            inverse[i].append(float(transposed[i][j]) / det)

    result = multiply(matrix_a, inverse)
    return result


def determinant(matrix):
    det = 0
    for i in range(len(matrix)):
        add = 1
        sub = 1
        for j in range(len(matrix)):
            add *= matrix[j][(i + j) % len(matrix)]
            sub *= matrix[j][(i - j) % len(matrix)]
        det += (add - sub)
    return det


def transpose(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    result = [[None] * rows for _ in range(cols)]
    for i in range(rows):
        for j in range(cols):
            result[j][i] = matrix[i][j]
    return result


def cofactor(matrix, row, col):
    addition = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if i != row and j != col:
                addition.append(matrix[i][j])
    result = ((-1) ** (row + col)) * (addition[0] * addition[3] - addition[2] * addition[1])
    return result


print(matrix_a)
print(matrix_b)

try:
    with open(constants.OUTPUT_FILE, 'w') as file:
        file.write("Addition:\n" + str(add(matrix_a, matrix_b)) + '\n')
        file.write("Subtraction:\n" + str(subtract(matrix_a, matrix_b)) + '\n')
        file.write("Multiplication:\n" + str(multiply(matrix_a, matrix_b)) + '\n')
        file.write("Division:\n" + str(divide(matrix_a, matrix_b)) + '\n')

except FileNotFoundError:
    raise FileNotFoundError
