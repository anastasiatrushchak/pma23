import const


class Matrix:
    def __init__(self, array):
        self.array = array

    def __add__(self, other):
        result = [[0 for i in range(len(self.array[0]))] for j in range(len(self.array))]
        for i in range(len(self.array)):
            for j in range(len(self.array[0])):
                try:
                    result[i][j] = self.array[i][j] + other.array[i][j]
                except IndexError:
                    print(const.INDEX_ERROR)
                    exit(-1)
        return result

    def __sub__(self, other):
        result = [[0 for i in range(len(self.array[0]))] for j in range(len(self.array))]
        for i in range(len(self.array)):
            for j in range(len(self.array[0])):
                try:
                    result[i][j] = self.array[i][j] - other.array[i][j]
                except IndexError:
                    print(const.INDEX_ERROR)
                    exit(-1)
        return result

    def __mul__(self, other):
        result = [[0 for i in range(len(other.array[0]))] for j in range(len(self.array))]
        for i in range(len(self.array)):
            for j in range(len(other.array[0])):
                for k in range(len(other.array)):
                    result[i][j] += self.array[i][k] * other.array[k][j]
        return result

    def __truediv__(self, other):
        result = [[0 for i in range(len(other.array[0]))] for j in range(len(self.array))]
        for i in range(len(self.array)):
            for j in range(len(Matrix.getMatrixInverse(other.array)[0])):
                for k in range(len(Matrix.getMatrixInverse(other.array))):
                    result[i][j] += self.array[i][k] * Matrix.getMatrixInverse(other.array)[k][j]
        return result

    @staticmethod
    def transposeMatrix(matrix):
        transpose = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
        print("\n")
        for row in transpose:
            return transpose

    @staticmethod
    def getMatrixMinor(m, i, j):
        return [row[:j] + row[j + 1:] for row in (m[:i] + m[i + 1:])]

    @staticmethod
    def getMatrixDeternminant(matrix):
        if len(matrix) == 2:
            return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

        determinant = 0
        for c in range(len(matrix)):
            try:
                determinant += ((-1) ** c) * matrix[0][c] * Matrix.getMatrixDeternminant(Matrix.getMatrixMinor(matrix, 0, c))
            except IndexError:
                print(const.INDEX_ERROR)
                exit(-1)
        return determinant

    @staticmethod
    def getMatrixInverse(matrix):
        determinant = Matrix.getMatrixDeternminant(matrix)
        try:
            if len(matrix) == 2:
                return [[matrix[1][1] / determinant, -1 * matrix[0][1] / determinant],
                        [-1 * matrix[1][0] / determinant, matrix[0][0] / determinant]]
        except ZeroDivisionError:
            print(const.ZERO_DIVISION)
            exit(-1)

        cofactors = []
        for r in range(len(matrix)):
            cofactorRow = []
            for c in range(len(matrix)):
                minor = Matrix.getMatrixMinor(matrix, r, c)
                cofactorRow.append(((-1) ** (r + c)) * Matrix.getMatrixDeternminant(minor))
            cofactors.append(cofactorRow)
        cofactors = Matrix.transposeMatrix(cofactors)
        for r in range(len(cofactors)):
            for c in range(len(cofactors)):
                try:
                    cofactors[r][c] = cofactors[r][c] / determinant
                except ZeroDivisionError:
                    print(const.ZERO_DIVISION)
                    exit(-1)
        return cofactors

    @staticmethod
    def read(name_file):
        a = []
        try:
            with open(name_file, 'r') as input_file:
                k = input_file.readline()
                while k != '':
                    temp = k.replace('\n', '').split(" ")
                    a.append([float(i) for i in temp if i.isdigit()])
                    k = input_file.readline()
        except FileNotFoundError:
            print(const.FILE_NOT_FOUND)
        return Matrix(a)

    @staticmethod
    def write(matrix_a, matrix_b, name_file):
        with open(name_file, 'w') as output_file:
            output_file.write("Addition: \n")
            for i in (matrix_a + matrix_b):
                output_file.write(str(i) + '\n')

            output_file.write("Subtraction: \n")
            for i in (matrix_a - matrix_b):
                output_file.write(str(i) + '\n')

            output_file.write("Multiplication: \n")
            for i in (matrix_a * matrix_b):
                output_file.write(str(i) + '\n')

            output_file.write("Division: \n")
            for i in (matrix_a / matrix_b):
                output_file.write(str(i) + '\n')

