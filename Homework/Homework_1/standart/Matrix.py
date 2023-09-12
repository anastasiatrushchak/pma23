import random
class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix
        self.row = len(matrix)
        self.column = len(matrix[0])

    @classmethod
    def random(cls, row, column, a=1, b=9):
        matrix = [[random.randint(a, b) for _ in range(column)] for _ in range(row)]
        return cls(matrix)
    @classmethod
    def from_file(cls, file_name):
        with open(file_name, 'r') as file:
            lines = file.readlines()
        matrix = []

        for line in lines:
            matrix_temp = [int(element) for element in line.split(" ")]
            matrix.append(matrix_temp)
        return cls(matrix)

    def __str__(self):
        matrix_str = ""
        for row in self.matrix:
            matrix_str += "\t".join(map(str, row)) + "\n"
        return matrix_str
    def __mul__(self, other):
        if isinstance(other, Matrix):
            if self.row != other.column | self.column != other.row != self.column:
                return None
            result = [[0 for _ in range(self.column)] for _ in range(self.row)]
            for i in range(self.column):
                for j in range(other.row):
                    result[i][j] = sum(self.matrix[i][k] * other.matrix[k][j] for k in range(self.column))
            return Matrix(result)
        elif isinstance(other, (int, float)):
            result = Matrix(self.column, self.row)
            for i in range(0, self.column):
                for j in range(0, self.row):
                    result.matrix[i][j] = self.matrix[i][j] * other
            return result
        return None

    def __add__(self, other):
        if isinstance(other, Matrix):
            if self.row != other.row | self.column != other.column:
                return None
            result = [[0 for _ in range(self.column)] for _ in range(self.row)]
            for i in range(0, self.column):
                for j in range(0, self.row):
                    result[i][j] = self.matrix[i][j] + other.matrix[i][j]
            return Matrix(result)
        elif isinstance(other, (int, float)):
            result = Matrix(self.column, self.row)
            for i in range(0, self.column):
                for j in range(0, self.row):
                    result.matrix[i][j] = self.matrix[i][j] + other
            return result
        return None

    def __sub__(self, other):
        if isinstance(other, Matrix):
            if self.row != other.row | self.column != other.column:
                return None
            result = [[0 for _ in range(self.column)] for _ in range(self.row)]
            for i in range(0, self.column):
                for j in range(0, self.row):
                    result[i][j] = self.matrix[i][j] - other.matrix[i][j]
            return Matrix(result)
        elif isinstance(other, (int, float)):
            result = Matrix(self.column, self.row)
            for i in range(0, self.column):
                for j in range(0, self.row):
                    result.matrix[i][j] = self.matrix[i][j] - other
            return result
    def __truediv__(self, other):
        if isinstance(other, Matrix):
            return Matrix(self * other.inverse())
        elif isinstance(other, (int, float)):
            return Matrix(self.matrix/other)

    @staticmethod
    def det(matrix):
        size = len(matrix)
        if size == 2:
            return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
        det = 0
        for j in range(size):
            submatrix = [[matrix[i][k] for k in range(size) if k != j] for i in range(1, size)]
            submatrix_det = Matrix.det(submatrix)
            det += ((-1) ** j) * matrix[0][j] * submatrix_det
        return det


    def transpose(matrix):
        rows, cols = len(matrix), len(matrix[0])
        transpose = [[0] * rows for _ in range(cols)]

        for i in range(rows):
            for j in range(cols):
                transpose[j][i] = matrix[i][j]

        return transpose


    def minor(self, row, col):
        minor = []
        for i in range(row):
            if i != row:
                minor_row = []
                for j in range(self.column):
                    if j != col:
                        minor_row.append(self.matrix[i][j])
                minor.append(minor_row)
        return minor
    def inverse(self):
        if(self.row != self.column):
            return None
        determinant = Matrix.det(self.matrix)
        if determinant == 0:
            return None

        self.row, self.column = len(self.matrix), len(self.matrix[0])
        temp = [[0] * self.column for _ in range(self.row)]

        for i in range(self.row):
            for j in range(self.column):
                cofactor = ((-1) ** (i + j)) * Matrix.det(self.minor(i, j))
                temp[j][i] = cofactor

        inverse = [[value / determinant for value in row] for row in temp]
        return Matrix(inverse)