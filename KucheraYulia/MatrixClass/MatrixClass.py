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

    def inverse(self):
        if len(self.matrix) != len(self.matrix[0]):
            raise ValueError("Матриця не є квадратною, обернена матриця не існує.")

        n = len(self.matrix)
        identity = [[1 if i == j else 0 for j in range(n)] for i in range(n)]

        augmented_matrix = [row[:] + identity_row for row, identity_row in zip(self.matrix, identity)]

        for col in range(n):
            pivot_row = col
            for row in range(col + 1, n):
                if abs(augmented_matrix[row][col]) > abs(augmented_matrix[pivot_row][col]):
                    pivot_row = row
            augmented_matrix[pivot_row], augmented_matrix[col] = augmented_matrix[col], augmented_matrix[pivot_row]

            pivot_elem = augmented_matrix[col][col]
            if pivot_elem == 0:
                raise ValueError("обернена матриця не існує.")

            pivot_row_scale = [elem / pivot_elem for elem in augmented_matrix[col]]
            for row in range(n):
                if row != col:
                    row_scale = [elem * augmented_matrix[row][col] for elem in pivot_row_scale]
                    augmented_matrix[row] = [elem1 - elem2 for elem1, elem2 in zip(augmented_matrix[row], row_scale)]

        inv_matrix = [row[n:] for row in augmented_matrix]
        return Matrix(inv_matrix)

    def __truediv__(self, other):
        inverse_other = other.inverse()
        return self.__mul__(inverse_other)


file_exists("InputM.txt")
file_exists("InputM2.txt")
file_exists("OutputMC.txt")

X = Matrix(read_matrix("InputM.txt"))
Y = Matrix(read_matrix("InputM2.txt"))

with open('OutputMC.txt', 'a') as f:
    print("add:", file=f)
    print(X + Y, file=f)
    print("sub:", file=f)
    print(X - Y, file=f)
    print("mult:", file=f)
    print(X * Y, file=f)
    print("div:", file=f)
    print(X / Y, file=f)