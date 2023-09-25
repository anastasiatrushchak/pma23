INPUT = 'input_matrix.txt'
OUT = 'out_matrix.txt'
FILE_NOT_FOUND_ERROR = 'File not found'
INDEX_ERROR = 'list index ot of range'
ZERO_DIVISION_ERROR = 'division by zero'
TYPE_ERROR = 'NoneType object is not subscriptable'
try:
    with open(INPUT, 'r') as f:
        matrix = [[int(num) for num in line.split()] for line in f]
        matrix_a = []
        matrix_b = []

        for x in range(len(matrix)):
            if matrix[x] == []:
                matrix_b = matrix[x + 1:]
                break
            matrix_a.append(matrix[x])
except FileNotFoundError:
    print(FILE_NOT_FOUND_ERROR)
    exit(-1)


def matrix_sum(matrix_a, matrix_b):
    try:
        return [[matrix_a[i][j] + matrix_b[i][j] for j in range(len(matrix_a[0]))] for i in range(len(matrix_a))]
    except IndexError:
        print(INDEX_ERROR)
        exit(-1)


def matrix_diff(matrix_a, matrix_b):
    try:
        return [[matrix_a[i][j] - matrix_b[i][j] for j in range(len(matrix_a[0]))] for i in range(len(matrix_a))]
    except IndexError:
        print(INDEX_ERROR)
        exit(-1)


def matrix_multiply(matrix_a, matrix_b):
    try:
        result = []
        for i in range(len(matrix_a)):
            row = []
            for j in range(len(matrix_b[0])):
                product = 0
                for v in range(len(matrix_a[i])):
                    product += matrix_a[i][v] * matrix_b[v][j]
                row.append(product)
            result.append(row)
        return result
    except TypeError:
        print(TYPE_ERROR)
        exit(-1)


def transpose_matrix(matrix):
    transpose = list(map(list, zip(*matrix)))
    return transpose


def minor_matrix(matrix, i, j):
    return [row[:j] + row[j+1:] for row in (matrix[:i] + matrix[i + 1:])]


def determinant_matrix(matrix):
    if len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    determinant = 0
    for c in range(len(matrix)):
        try:
            determinant += ((-1)**c) * matrix[0][c] * determinant_matrix(minor_matrix(matrix, 0, c))
        except IndexError:
            print(INDEX_ERROR)
            exit(-1)
    return determinant


def inverse_matrix(matrix):
        determinant = determinant_matrix(matrix)
        if determinant == 0:
            return

        if len(matrix) == 2:
            return [[matrix[1][1] / determinant, -1 * matrix[0][1] / determinant],
                    [-1 * matrix[1][0] / determinant, matrix[0][0] / determinant]]
        cofactors = []
        for r in range(len(matrix)):
            cofactor_row = []
            for c in range(len(matrix)):
                minor = minor_matrix(matrix, r, c)
                cofactor_row.append(((-1)**(r+c)) * determinant_matrix(minor))
            cofactors.append(cofactor_row)

        result = transpose_matrix(cofactors)

        for r in range(len(result)):
            for c in range(len(result)):
                try:
                    result[r][c] = result[r][c]/determinant
                except ZeroDivisionError:
                    print(ZERO_DIVISION_ERROR)
                    exit(-1)
        return result


def division(matrix_a, matrix_b):
    return matrix_multiply(matrix_a, inverse_matrix(matrix_b))



try:
    with open(OUT, 'w') as f:
        f.write("Sum of matrix: ")
        f.write(str(matrix_sum(matrix_a, matrix_b)))
        f.write("\n")
        f.write("Difference of matrix: ")
        f.write(str(matrix_diff(matrix_a, matrix_b)))
        f.write("\n")
        f.write("Multiply of matrix: ")
        f.write(str(matrix_multiply(matrix_a, matrix_b)))
        f.write("\n")
        f.write("Division of matrix: ")
        f.write(str(division(matrix_a, matrix_b)))
except FileNotFoundError:
    print(FILE_NOT_FOUND_ERROR)
    exit(-1)

'''    def transpose_matrix(self):
        transpose = list(map(list, zip(*self.matrix_b)))
        return transpose


    def minor_matrix(self, i, j):
        return [row[:j] + row[j+1:] for row in (self.matrix_b[:i] + self.matrix_b[i + 1:])]


    def determinant_matrix(self):
        if len(self.matrix_b) == 2:
            return self.matrix_b[0][0] * self.matrix_b[1][1] - self.matrix_b[0][1] * self.matrix_b[1][0]
        determinant = 0
        for c in range(len(self.matrix_b)):
            try:
                determinant += ((-1)**c) * self.matrix_b[0][c] * self.determinant_matrix(self.minor_matrix(self.matrix_b, 0, c))
            except IndexError:
                print(INDEX_ERROR)
                exit(-1)
        return determinant


    def inverse_matrix(self):
        determinant = self.determinant_matrix(self.matrix_b)
        if determinant == 0:
            return

        if len(self.matrix_b) == 2:
            return [[self.matrix_b[1][1] / determinant, -1 * self.matrix_b[0][1] / determinant],
                    [-1 * self.matrix_b[1][0] / determinant, self.matrix_b[0][0] / determinant]]
        cofactors = []
        for r in range(len(self.matrix_b)):
            cofactor_row = []
            for c in range(len(self.matrix_b)):
                minor = self.minor_matrix(self.matrix_b, r, c)
                cofactor_row.append(((-1)**(r+c)) * self.determinant_matrix(minor))
            cofactors.append(cofactor_row)

        result = self.transpose_matrix(cofactors)

        for r in range(len(result)):
            for c in range(len(result)):
                try:
                    result[r][c] = result[r][c]/determinant
                except ZeroDivisionError:
                    print(ZERO_DIVISION_ERROR)
                    exit(-1)
        return result'''
