import numpy as np

class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix
        self.row = matrix.shape[0]
        self.column = matrix.shape[1]

    @classmethod
    def random(cls, row, column):
        matrix = np.random.randint(1, 11, size=(row, column))
        return cls(matrix)
    @classmethod
    def from_file(cls, file_name):
        matrix = np.loadtxt(file_name, dtype='i', delimiter=' ')
        return cls(matrix)

    @classmethod
    # def default(cls):
    #     print("Input row: ")
    #
    def print(self):
        for i in range(0, self.row):
            for j in range(0, self.column):
                print(self.matrix[i][j], end="\t")
            print()

    def addition(self, other):
        if self.row == other.row and self.column == other.column:
            return Matrix(self.matrix + other.matrix)
        return None

    def subtraction(self, other):
        if self.row == other.row and self.column == other.column:
            return Matrix(self.matrix - other.matrix)
        return None

    def division(self, other):
        if self.row == other.row and self.column == other.column:
            return Matrix(np.divide(self.matrix, other.matrix))
        return None
    def multiplication(self, other):
        if self.row == other.column:
            return Matrix(self.matrix.dot(other.matrix))
        return None
    def inverse(self):
        if np.linalg.det(self.matrix) != 0:  # перевірка чи визначник матриці не 0
            return Matrix(np.linalg.inv(self.matrix))              # метод шукає матрицю в -1
        return None