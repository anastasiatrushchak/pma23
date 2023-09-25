class MatrixOperations:

    def __init__(self, matrix):
        self.matrix = matrix

    def __add__(self, matrix2):
        return [[k + n for k, n in zip(i, j)] for i, j in zip(self.matrix, matrix2.matrix)]


    def __sub__(self, matrix2):
        return [[k - n for k, n in zip(i, j)] for i, j in zip(self.matrix, matrix2.matrix)]


    def __mul__(self, matrix2):
        m, n, p = len(self.matrix), len(matrix2.matrix), len(matrix2.matrix[0])
        if n != len(matrix2.matrix):
            raise ValueError("Number of columns in the first matrix must be equal to the number of rows in the second matrix.")
        result = []
        for l_row in range(m):
            temp_row = []
            for k in range(p):
                sum1 = 0
                for l_col in range(n):
                    sum1 = sum1 + (self.matrix[l_row][l_col] * matrix2.matrix[l_col][k])
                temp_row.append(sum1)
            result.append(temp_row)
        return result


    def transpose_matrix(self):
        return [[self.matrix[j][i] for j in range(len(self.matrix))] for i in range(len(self.matrix[0]))]


    def __truediv__(self, scalar):
        return [[element / scalar for element in row] for row in self.matrix]


import copy

# class MatrixOperationsExtended(MatrixOperations):
#
#     def divide_matrix_by_determinant(matrix, determinant):
#         return [[element / determinant for element in row] for row in matrix]
#
#
#     def __add__(self, matrix2):
#         return MatrixOperations.sum_matrix(self, matrix2)
#
#
#     def __sub__(self, matrix2):
#         return MatrixOperations.subtract_matrix(self, matrix2)
#
#
#     def __mul__(self, matrix1, matrix2):
#         return MatrixOperations.multiply_matrix(matrix1, matrix2)
#
#     def __truediv__(self, matrix, scalar):
#         return MatrixOperations.divide_matrix_by_scalar(matrix, scalar)

INPUT_MATRIX_first = "inputMatrix1.txt"
INPUT_MATRIX_second = "inputMatrix2.txt"

try:
    firstMatrix = []
    with open(INPUT_MATRIX_first, "r") as firstFileMatrix:
        for line in firstFileMatrix:
            row = [int(x) for x in line.split()]
            firstMatrix.append(row)
except FileNotFoundError:
    print("File " + INPUT_MATRIX_first + " not found")
    exit(-1)

try:
    secondMatrix = []
    with open(INPUT_MATRIX_second, "r") as secondFileMatrix:
        for line in secondFileMatrix:
            row = [int(x) for x in line.split()]
            secondMatrix.append(row)
except FileNotFoundError:
    print("File " + INPUT_MATRIX_second + " not found")
    exit(-1)

# sum_result = sum_matrix(firstMatrix, secondMatrix)
# substruct_result = substruct_matrix(firstMatrix, secondMatrix)


# sum_result = MatrixOperations.sum_matrix(firstMatrix, secondMatrix)
# substruct_result = MatrixOperations.subtract_matrix(firstMatrix, secondMatrix)
# multiply_result = MatrixOperations.multiply_matrix(firstMatrix, secondMatrix)

firstMatrixClass = MatrixOperations(firstMatrix)
secondMatrixClass = MatrixOperations(secondMatrix)


sum_result = firstMatrixClass + secondMatrixClass
substract_result = firstMatrixClass - secondMatrixClass
multiply_result = firstMatrixClass * secondMatrixClass

m = len(firstMatrix)
n = len(secondMatrix)
p = len(secondMatrix[0])
if m != n:
    raise ValueError("Matrices have different numbers of rows.")
resultMatrix = []
for l_row in range(m):
    temp_row = []
    for k in range(p):
        sum1 = 0
        for l_col in range(n):
            sum1 = sum1 + (firstMatrix[l_row][l_col] * secondMatrix[l_col][k])

        temp_row.append(sum1)
    resultMatrix.append(temp_row)

# division of the matrix
secondMatrixd = []
with open(INPUT_MATRIX_second, "r") as secondFileMatrix:
    for line in secondFileMatrix:
        row = [int(x) for x in line.split()]
        secondMatrixd.append(row)


def copy_matrix(matrix):
    return [row[:] for row in matrix]


def determinant_fast(matrix):
    n = len(matrix)
    AM = copy_matrix(matrix)
    for fd in range(n):
        for i in range(fd + 1, n):
            if AM[fd][fd] == 0:
                return 0.0
            crScaler = AM[i][fd] / AM[fd][fd]
            for j in range(n):
                AM[i][j] = AM[i][j] - crScaler * AM[fd][j]
    product = 1.0
    for i in range(n):
        product *= AM[i][i]
    return product


determinant_result = determinant_fast(secondMatrixd)


def algebraic_cofactor(matrix, row, col):
    submatrix = [row[:col] + row[col + 1:] for row in (matrix[:row] + matrix[row + 1:])]
    sign = (-1) ** (row + col)
    return sign * determinant_fast(submatrix)


determinant_result = determinant_fast(secondMatrix)

algebraic_result = []
for i in range(n):
    temp_row = []
    for j in range(p):
        temp_row.append(algebraic_cofactor(secondMatrix, i, j))
    algebraic_result.append(temp_row)


def transpose(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    transposed_matrix = [[matrix[j][i] for j in range(rows)] for i in range(cols)]
    return transposed_matrix


transposed_algebraic_result = transpose(algebraic_result)
print(transposed_algebraic_result)

try:
    def divide_matrix_by_determinant(matrix, determinant_result):
        rows = len(matrix)
        cols = len(matrix[0])
        last_matrix = []
        for i in range(rows):
            temp_row = []
            for j in range(cols):
                temp_row.append(matrix[i][j] / determinant_result)
            last_matrix.append(temp_row)
        return last_matrix
except ZeroDivisionError:
    print("Error: Division by zero (determinant is zero).")
last_matrix = divide_matrix_by_determinant(transposed_algebraic_result, determinant_result)
firstMatrix = []
with open(INPUT_MATRIX_first, "r") as firstFileMatrix:
    for line in firstFileMatrix:
        row = [int(x) for x in line.split()]
        firstMatrix.append(row)
k = len(firstMatrix)
y = len(secondMatrix)
s = len(secondMatrix[0])
resultMatrixdva = []
for l_row in range(k):
    temp_row = []
    for k in range(s):
        sum1 = 0
        for l_col in range(y):
            sum1 = sum1 + (firstMatrix[l_row][l_col] * last_matrix[l_col][k])

        temp_row.append(sum1)
    resultMatrixdva.append(temp_row)

with open("output.txt", "w") as f:
    f.write("Result of Multiplication:\n")
    for row in resultMatrix:
        f.write(" ".join(map(str, row)) + "\n")
    f.write("\nResult of Division:\n")
    for row in resultMatrixdva:
        f.write(" ".join(map(str, row)) + "\n")
    f.write("\nSum Result:\n")
    for row in sum_result:
        f.write(" ".join(map(str, row)) + "\n")
    f.write("\nSubtraction Result:\n")
    for row in substract_result:
        f.write(" ".join(map(str, row)) + "\n")
