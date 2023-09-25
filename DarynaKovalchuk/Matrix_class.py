import os

class DetIsZero(Exception):
    def init(self, message="Determinant is zero!"):
        self.message = message
        super().init(self.message)

class Matrix:
    def init(self, filename):
        self.matrix = self.read_matrix(filename)

    def read_matrix(self, filename):
        with open(filename, 'r') as file:
            lines = file.readlines()
        matrix = []
        for line in lines:
            rows = [int(x) for x in line.split()]
            matrix.append(rows)
        return matrix

    def write_matrix(self, filename, result_matrix):
        with open(filename, 'a') as file:
            file.write("matrix result:\n")
            for rows in result_matrix:
                file.write(' '.join(map(str, rows)) + '\n')

    def add(self, other_matrix):
        result = []
        for i in range(len(self.matrix)):
            row = []
            for j in range(len(self.matrix[0])):
                row.append(self.matrix[i][j] + other_matrix[i][j])
            result.append(row)
        return result

    def sub(self, other_matrix):
        result = []
        for i in range(len(self.matrix)):
            row = []
            for j in range(len(self.matrix[0])):
                row.append(self.matrix[i][j] - other_matrix[i][j])
            result.append(row)
        return result

    def mul(self, other_matrix):
        result = []
        for i in range(len(self.matrix)):
            row = []
            for j in range(len(other_matrix[0])):
                sum_element = 0
                for k in range(len(other_matrix)):
                    sum_element += self.matrix[i][k] * other_matrix[k][j]
                row.append(sum_element)
            result.append(row)
        return result

    def truediv(self, other_matrix):
        try:
            transposed = [
                [other_matrix[1][1], -other_matrix[1][0]],
                [-other_matrix[0][1], other_matrix[0][0]]
            ]
            det = other_matrix[0][0] * other_matrix[1][1] - other_matrix[0][1] * other_matrix[1][0]

            if det == 0:
                raise DetIsZero

            inverse = []
            for i in range(len(transposed)):
                inverse.append([])
                for j in range(len(transposed[0])):
                    inverse[i].append(transposed[j][i] / det)
            result = self.mul(inverse)
            return result

        except DetIsZero as e:
            print("Det can't be zero!")
            return []

try:
    first_matrix = Matrix('first_matrix.txt')
    second_matrix = Matrix('second_matrix.txt')
except FileNotFoundError:
    print("One or both files do not exist.")
    exit()

if not first_matrix.matrix or not second_matrix.matrix:
    print("One or both files are empty.")
    exit()

if len(first_matrix.matrix) != len(second_matrix.matrix) or len(first_matrix.matrix[0]) != len(second_matrix.matrix[0]):
    print("The sizes don't match.")
else:
    result_addition = first_matrix + second_matrix.matrix
    result_subtraction = first_matrix - second_matrix.matrix
    result_multiply = first_matrix * second_matrix.matrix
    result_devide = first_matrix / second_matrix.matrix

    first_matrix.write_matrix('result_addition.txt', result_addition)
    first_matrix.write_matrix('result_subtraction.txt', result_subtraction)
    first_matrix.write_matrix('result_multiply.txt', result_multiply)
    first_matrix.write_matrix('result_divide.txt', result_devide)

    print("Result addition:")
    for rows in result_addition:
        print(rows)

    print("Result subtraction:")
    for rows in result_subtraction:
        print(rows)

    print("Result multiply:")
    for rows in result_multiply:
        print(rows)

    print("Result divide:")
    for rows in result_devide:
        print(rows)
