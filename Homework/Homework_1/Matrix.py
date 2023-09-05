import numpy as np

class Matrix:
    def __init__(self, row, column):
        self.row = row
        self.column = column
        self.matrix = np.random.randint(1, 11, size=(row, column))

    def print(self):
        for i in range(0, self.row):
            for j in range(0, self.column):
                print(self.matrix[i][j], end="\t")
            print()

    def addition(self, other):
        if self.row == other.row and self.column == other.column:
            result = Matrix(self.row, self.column)
            result.matrix = self.matrix + other.matrix
            return result
        return None

    def subtraction(self, other):
        if self.row == other.row and self.column == other.column:
            result = Matrix(self.row, self.column)
            result.matrix = self.matrix - other.matrix
            return result
        return None

    def division(self, other):
        if self.row == other.row and self.column == other.column:
            result = Matrix(self.row, self.column)
            result.matrix = self.matrix / other.matrix
            return result
        return None
    def multiplication(self, other):
        result = Matrix(self.row, self.column)
        result.matrix = self.matrix.dot(other.matrix)
        return result
