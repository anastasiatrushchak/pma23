import random


from Homework.Homework_1.Exception import InvalidSize, InvalidMatrixInverse, InvalidType

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
    def str_to_file(self, file_name="result.txt"):
        with open(file_name, 'w') as writeFile:
            writeFile.write(str(self))
    def __str__(self):
        matrix_str = ""
        for row in self.matrix:
            matrix_str += "\t".join(map(str, row)) + "\n"
        return matrix_str
    def __mul__(self, other):
        if isinstance(other, Matrix):
            if self.row != other.column | self.column != other.row != self.column:
                raise InvalidSize("Size error")
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
        raise InvalidType("Type error")

    def __add__(self, other):
        if isinstance(other, Matrix):
            if self.row != other.row | self.column != other.column:
                raise InvalidSize("Size error")
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
        raise InvalidType("Type error")
    def __sub__(self, other):
        if isinstance(other, Matrix):
            if self.row != other.row | self.column != other.column:
                raise InvalidSize("Size error")
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
            return self * other.inverse()
        elif isinstance(other, (int, float)):
            return Matrix(self.matrix/other)
    def inverse(self):
        if self.row != self.column:
            raise InvalidSize("Size error")
        identity_matrix = [[0] * self.column for _ in range(self.row)]
        for i in range(self.row):
            identity_matrix[i][i] = 1

        matrix_copy = [row[:] for row in self.matrix]
        identity_copy = [row[:] for row in identity_matrix]

        for i in range(self.row):
            pivot = matrix_copy[i][i]
            if pivot == 0:
                raise InvalidMatrixInverse("Inverse error")
            for j in range(self.column):
                matrix_copy[i][j] /= pivot
                identity_copy[i][j] /= pivot

            for k in range(self.row):
                if k != i:
                    factor = matrix_copy[k][i]
                    for j in range(self.column):
                        matrix_copy[k][j] -= factor * matrix_copy[i][j]
                        identity_copy[k][j] -= factor * identity_copy[i][j]

        return Matrix(identity_copy)
