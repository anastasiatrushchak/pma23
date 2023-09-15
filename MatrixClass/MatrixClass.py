import os


def file_exists(filename):
    if os.path.isfile(filename):
        print("Файл існує.")
        with open(filename, 'r') as file:
            if file.read() == "":
                print("Файл порожній.")
            else:
                print("Файл не порожній.")
    else:
        print("Файл не існує.")


def read_matrix(filename):
    matrix = []
    with open(filename, 'r') as file:
        for line in file:
            row = list(map(int, line.split()))
            matrix.append(row)
    return matrix


class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return '\n'.join(['\t'.join(map(str, row)) for row in self.matrix])

    def __add__(self, other):
        if len(self.matrix) != len(other.matrix) or len(self.matrix[0]) != len(other.matrix[0]):
            raise ValueError("Розміри матриць повинні співпадати для додавання.")
        result = []
        for i in range(len(self.matrix)):
            row = []
            for j in range(len(self.matrix[0])):
                row.append(self.matrix[i][j] + other.matrix[i][j])
            result.append(row)
        return Matrix(result)

    def __sub__(self, other):
        if len(self.matrix) != len(other.matrix) or len(self.matrix[0]) != len(other.matrix[0]):
            raise ValueError("Розміри матриць повинні співпадати для віднімання.")
        result = []
        for i in range(len(self.matrix)):
            row = []
            for j in range(len(self.matrix[0])):
                row.append(self.matrix[i][j] - other.matrix[i][j])
            result.append(row)
        return Matrix(result)

    def __mul__(self, other):
        if len(self.matrix[0]) != len(other.matrix):
            raise ValueError(
                "Кількість стовпців першої матриці повинна дорівнювати кількості рядків другої матриці для множення.")
        result = []
        for i in range(len(self.matrix)):
            row = []
            for j in range(len(other.matrix[0])):
                row.append(sum(self.matrix[i][k] * other.matrix[k][j] for k in range(len(other.matrix))))
            result.append(row)
        return Matrix(result)


file_exists("InputM.txt")
file_exists("InputM2.txt")
file_exists("OutputM.txt")

X = Matrix(read_matrix("InputM.txt"))
Y = Matrix(read_matrix("InputM2.txt"))

print(X + Y)
print(X)
print(Y)