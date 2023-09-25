import os

MATRIX_ONE_FILE = "matrix_one.txt"
MATRIX_TWO_FILE = "matrix_two.txt"
RESULT_FILE = "result.txt"


def read_file(filename):
    try:
        matrix = []
        if not os.path.exists(filename):
            raise Exception("Error!", filename, " is not found!")
        with open(filename) as file:
            for i in range(3):
                line = file.readline()
                matrix.append(line.split())
                matrix[i] = [float(j) for j in matrix[i] if j.isdigit]
        return matrix
    except Exception as err:
        print(err)


def push_to_file(matrix):
    with open(RESULT_FILE, "w") as file:
        for i in matrix:
            file.write(str(i))
            file.write('\n')


class Matrix:

    def __init__(self, matrix=[[], [], []]):
        self.matrix = matrix

    def __get_det(self, mtrx):
        det = 0
        size = len(mtrx)
        if size == 2:
            return mtrx[0][0] * mtrx[1][1] - mtrx[0][1] * mtrx[1][0]
        elif size == 3:
            for i in range(3):
                det += mtrx[0][i] * (
                        mtrx[1][(i + 1) % 3] * mtrx[2][(i + 2) % 3] - mtrx[1][(i + 2) % 3] * mtrx[2][
                        (i + 1) % 3])
            return det
        elif size > 3:
            raise Exception("Error! Matrix size is >3")

    def __add__(self, other):
        matrix = []
        for i in range(3):
            matrix.append([self.matrix[i][j] + other.matrix[i][j] for j in range(3)])
        return matrix

    def __sub__(self, other):
        matrix = []
        for i in range(3):
            matrix.append([self.matrix[i][j] - other.matrix[i][j] for j in range(3)])
        return matrix

    def __mul__(self, other):
        matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        for i in range(3):
            for j in range(3):
                for k in range(3):
                    matrix[i][j] += self.matrix[i][k] * other.matrix[k][j]
        return matrix

    def __truediv__(self, other):
        try:
            matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
            n = 3
            det = self.__get_det(other.matrix)
            if det == 0:
                raise Exception("Error! Det == 0! Dividing is impossible")
            adj_matrix = []
            for j in range(n):
                adj_row = []
                for i in range(n):
                    submatrix = [row[:j] + row[j + 1:] for row in (other.matrix[:i] + other.matrix[i + 1:])]
                    cofactor = self.__get_det(submatrix) * (-1) ** (i + j)
                    adj_row.append(cofactor)
                adj_matrix.append(adj_row)
            for i in range(3):
                for j in range(3):
                    for k in range(3):
                        matrix[i][j] += self.matrix[i][k] * adj_matrix[k][j]
            return matrix
        except Exception as err:
            print(err)


a = Matrix(read_file(MATRIX_ONE_FILE))
b = Matrix(read_file(MATRIX_TWO_FILE))
push_to_file(a+b)
