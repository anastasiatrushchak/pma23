MATRIX_ONE = 'matrix_one.txt'
MATRIX_TWO = 'matrix_two.txt'
RESULT_FILE = 'result.txt'
MODE_READ = 'r'
MODE_WRITE = 'w'
FILE_ERROR = 'File Not Found'


class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        matrix = []
        for i in self.matrix:
            row = str(i)
            matrix.append(row)
        return "\n".join(matrix)

    def __add__(self, other):
        result = []
        for i in range(len(self.matrix)):
            row = []
            for j in range(len(self.matrix[0])):
                row.append(self.matrix[i][j] + other.matrix[i][j])
            result.append(row)
        return Matrix(result)

    def __sub__(self, other):
        result = []
        for i in range(len(self.matrix)):
            row = []
            for j in range(len(self.matrix[0])):
                row.append(self.matrix[i][j] - other.matrix[i][j])
            result.append(row)
        return Matrix(result)

    def __mul__(self, other):
        result = []
        for i in range(len(self.matrix)):
            row = []
            for j in range(len(other.matrix[0])):
                sum = 0
                for k in range(len(other.matrix)):
                    sum += self.matrix[i][k] * other.matrix[k][j]
                row.append(sum)
            result.append(row)
        return Matrix(result)

    def det(self):
        n = len(self.matrix)
        if n == 1:
            return self.matrix[0][0]
        elif n == 2:
            return self.matrix[0][0] * self.matrix[1][1] - self.matrix[0][1] * self.matrix[1][0]
        else:
            determinant = 0
            for j in range(n):
                submatrix = [[self.matrix[i][k] for k in range(n) if k != j] for i in range(1, n)]
                sign = (-1) ** j
                determinant += sign * self.matrix[0][j] * Matrix(submatrix).det()
            return determinant

    def algebraic_dopovnenia(self):
        n = len(self.matrix)
        alg_dopov = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                submatrix = [[self.matrix[k][l] for l in range(n) if l != j] for k in range(n) if k != i]
                sign = (-1) ** (i + j)
                alg_dopov[j][i] = sign * Matrix(submatrix).det()
        return alg_dopov

    def inverse(self):
        determinant = Matrix(self.matrix).det()
        alg_dopov = Matrix(self.matrix).algebraic_dopovnenia()
        inverse_matrix = []
        n = len(alg_dopov)
        for i in range(n):
            row = []
            for j in range(n):
                row.append(alg_dopov[i][j] / determinant)
            inverse_matrix.append(row)
        return Matrix(inverse_matrix)

    def reading(file_name):
        matrix = []
        with open(file_name, 'r') as file:
            for i in file:
                row = [int(x) for x in i.split()]
                matrix.append(row)
        return Matrix(matrix)

    def writing(self, matrix_first, matrix_second, action, sign):
        file.write(action)
        file.write(str(matrix_first) + '\n')
        file.write(sign + '\n')
        file.write(str(matrix_second) + '\n')
        file.write('=' + '\n' + str(self) + '\n' + 50 * '-' + '\n')


try:
    matrix_one = Matrix.reading(MATRIX_ONE)
except FileNotFoundError:
    print(FILE_ERROR)
    exit(-1)
try:
    matrix_two = Matrix.reading(MATRIX_TWO)
except FileNotFoundError:
    print(FILE_ERROR)
    exit(-1)
add_res = matrix_one + matrix_two
sub_res = matrix_one - matrix_two
mult_res = matrix_one * matrix_two
try:
    deter = matrix_two.det()
    inverse_matrix = matrix_two.inverse()
    div_res = matrix_one * inverse_matrix
except ZeroDivisionError:
    print('Matrixes can not be divided')
    exit(-1)
try:
    with open(RESULT_FILE, MODE_WRITE) as file:
        add_res.writing(matrix_one, matrix_two, 'Addition:\n', '+')
        sub_res.writing(matrix_one, matrix_two, 'Substraction:\n', '-')
        mult_res.writing(matrix_one, matrix_two, 'Multiplying:\n', '*')
        div_res.writing(matrix_one, matrix_two, 'Division:\n', '/')
except FileNotFoundError:
    print(FILE_ERROR)
