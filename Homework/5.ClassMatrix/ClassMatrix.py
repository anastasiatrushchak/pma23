MATRIX_FIRST_INPUT='matrix1.txt'
MATRIX_SECOND_INPUT = 'matrix2.txt'
MATRIX_RESULT = 'matrix_rez.txt'
mode = 'r'
def print_matrix(matrix):
    for i in matrix:
        print(i)
class Matrix:
    def __init__(self, matrix=[]):
        self.matrix = matrix
    def __str__(self):
        return '\n'.join([' '.join(map(str, row)) for row in self.matrix])
    def read(self,MATRIX_INPUT):

        try:
            matrix = []
            with open(MATRIX_INPUT, "r") as lines:
                lines = lines.readlines()

                for line in lines:
                    row = [float(x) for x in line.split()]
                    matrix.append(row)
            self.matrix=matrix
        except FileNotFoundError:
            print("File " + MATRIX_FIRST_INPUT + "no found.")
            exit(-1)
    def __mul__(self, other):

        try:
            matrix_multiplication = []
            for i in range(len(self.matrix)):
                row = []
                for j in range(len(other.matrix[0])):
                    number = 0
                    for k in range(max(len(self.matrix[0]), len(other.matrix))):
                        number += float(self.matrix[i][k]) * float(other.matrix[k][j])
                    row.append(round(number, 3))
                matrix_multiplication.append(row)
            return Matrix(matrix_multiplication)
        except IndexError:
            print("The number of columns of the first matrix is not equal to the number of rows of the second matrix: " + str(len(self.matrix[0])) + '!=' + str(len(other.matrix)))

    def __truediv__(self, other):
        matrix = other.matrix
        n = len(matrix)


        inverse = [[0 for j in range(n)] for i in range(n)]
        for i in range(n):
            inverse[i][i] = 1

        for col in range(n):

            max_val = abs(matrix[col][col])
            max_row = col
            for k in range(col + 1, n):
                if abs(matrix[k][col]) > max_val:
                    max_val = abs(matrix[k][col])
                    max_row = k


            matrix[col], matrix[max_row] = matrix[max_row], matrix[col]
            inverse[col], inverse[max_row] = inverse[max_row], inverse[col]

            try:
                pivot = matrix[col][col]
                for j in range(n):
                    matrix[col][j] /= pivot
                    inverse[col][j] /= pivot
            except ZeroDivisionError:
                print("It is not possible to divide by zero")
                exit(-1)

            for i in range(n):
                if i != col:
                    factor = matrix[i][col]
                    for j in range(n):
                        matrix[i][j] -= factor * matrix[col][j]
                        inverse[i][j] -= factor * inverse[col][j]

        return Matrix(self.matrix) * Matrix(inverse)
    def __add__(self, other):
        try:
            matrix_sum = []
            for i in range(max(len(other.matrix), len(self.matrix))):
                row_matrix_rez = []
                for j in range(max(len(other.matrix[0]), len(self.matrix[0]))):
                    row_matrix_rez.append(float(self.matrix[i][j]) + float(other.matrix[i][j]))
                matrix_sum.append(row_matrix_rez)
            return Matrix(matrix_sum)
        except IndexError:
            print("It is not possible to add matrices.")
    def __sub__(self, other):
        try:
            matrix_difference = []
            for i in range(len(other.matrix)):
                row_matrix_rez = []
                for j in range(len(other.matrix[0])):
                    row_matrix_rez.append(float(self.matrix[i][j]) - float(other.matrix[i][j]))
                matrix_difference.append(row_matrix_rez)
            return Matrix(matrix_difference)
        except IndexError:
            print("It is not possible to subtract matrices.")
First_Matrix = Matrix()
Second_Matrix = Matrix()

First_Matrix.read(MATRIX_FIRST_INPUT)
Second_Matrix.read(MATRIX_SECOND_INPUT)

sum = First_Matrix + Second_Matrix
difference = First_Matrix - Second_Matrix
multipliation = First_Matrix * Second_Matrix
divide = First_Matrix / Second_Matrix
with open(MATRIX_RESULT, 'w') as file:
    file.write("Addition:\n" + str(sum)+'\n')
    file.write("Subtraction:\n" + str(difference)+'\n')
    file.write("Multiplication:\n" + str(multipliation) + '\n')
    file.write("Division:\n" + str(divide) + '\n')


