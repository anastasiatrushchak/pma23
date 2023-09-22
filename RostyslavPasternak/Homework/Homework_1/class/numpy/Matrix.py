import numpy as np

class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix
        self.row = matrix.shape[0]
        self.column = matrix.shape[1]

    @classmethod
    def random(cls, row, column, a=1, b=11):
        matrix = np.random.randint(a, b, size=(row, column))
        return cls(matrix)
    @classmethod
    def from_file(cls, file_name):
        matrix = np.loadtxt(file_name, dtype=int, delimiter=" ")
        return cls(matrix)
    def str_to_file(self, file_name="result.txt"):
        with open(file_name, 'w') as writeFile:
            writeFile.write(str(self))
    def __str__(self):
        matrix_str = ""
        for row in self.matrix:
            matrix_str += "\t".join(map(str, row)) + "\n"
        return matrix_str
    def __add__(self, other):
        if isinstance(other, Matrix):
            if self.row == other.row and self.column == other.column:
                return Matrix(self.matrix + other.matrix)
            return None
        elif isinstance(other, (int,float)):
            return Matrix(self.matrix + other)
    def __sub__(self, other):
        if isinstance(other, Matrix):
            if self.row == other.row and self.column == other.column:
                return Matrix(self.matrix - other.matrix)
            return None
        elif isinstance(other, (int,float)):
            return Matrix(self.matrix - other)
    def __truediv__(self, other):
        if isinstance(other, Matrix):
            if self.row == other.row and self.column == other.column:
                return Matrix(np.divide(self.matrix, other.matrix))
            return None
        elif isinstance(other, (int, float)):
            # return Matrix(np.divide(self.matrix, other))
            return Matrix(self.matrix/other)

    def __mul__(self, other):
        if isinstance(other, Matrix):
            if self.row == other.column:
                return Matrix(self.matrix.dot(other.matrix))
            return None
        elif isinstance(other, (int, float)):
            return Matrix(self.matrix.dot(other))
    def inverse(self):
        det = np.linalg.det(self.matrix)
        if det != 0:
            return Matrix(np.linalg.inv(self.matrix))
        return None