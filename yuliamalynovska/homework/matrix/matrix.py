import const_matrix
ZERO_DIVISION = 'float division by zero'
INDEX_ERROR = 'list index out of range'
FILE_NOT_FOUND_ERROR = 'the name of file is incorrect'
ATTRIBUTE_ERROR = 'module const_matrix has no such attribute'


def addition(matrix_a, matrix_b):
    result = [[0 for i in range(len(matrix_a[0]))] for j in range(len(matrix_a))]
    for i in range(len(matrix_a)):
        for j in range(len(matrix_a[0])):
            try:
                result[i][j] = matrix_a[i][j] + matrix_b[i][j]
            except IndexError:
                print(INDEX_ERROR)
                exit(-1)
    return result


def subtraction(matrix_a, matrix_b):
    result = [[0 for i in range(len(matrix_a[0]))] for j in range(len(matrix_a))]
    for i in range(len(matrix_a)):
        for j in range(len(matrix_a[0])):
            result[i][j] = matrix_a[i][j] - matrix_b[i][j]
    return result


def multiplication(matrix_a, matrix_b):
    result = [[0 for i in range(len(matrix_b[0]))] for j in range(len(matrix_a))]
    for i in range(len(matrix_a)):
        for j in range(len(matrix_b[0])):
            for k in range(len(matrix_b)):
                result[i][j] += matrix_a[i][k] * matrix_b[k][j]
    return result


def transposeMatrix(matrix):
    # return list(map(list, zip(*matrix)))
    transpose = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
    print("\n")
    for row in transpose:
        return transpose


def getMatrixMinor(m, i, j):
    return [row[:j] + row[j+1:] for row in (m[:i]+m[i+1:])]


def getMatrixDeternminant(matrix):
    if len(matrix) == 2:
        return matrix[0][0]*matrix[1][1]-matrix[0][1]*matrix[1][0]

    determinant = 0
    for c in range(len(matrix)):
        try:
            determinant += ((-1)**c)*matrix[0][c]*getMatrixDeternminant(getMatrixMinor(matrix, 0, c))
        except IndexError:
            print(INDEX_ERROR)
            exit(-1)
    return determinant


def getMatrixInverse(matrix):
    determinant = getMatrixDeternminant(matrix)
    try:
        if len(matrix) == 2:
            return [[matrix[1][1]/determinant, -1*matrix[0][1]/determinant],
                    [-1*matrix[1][0]/determinant, matrix[0][0]/determinant]]
    except ZeroDivisionError:
        print(ZERO_DIVISION)
        exit(-1)

    cofactors = []
    for r in range(len(matrix)):
        cofactorRow = []
        for c in range(len(matrix)):
            minor = getMatrixMinor(matrix, r, c)
            cofactorRow.append(((-1)**(r + c)) * getMatrixDeternminant(minor))
        cofactors.append(cofactorRow)
    cofactors = transposeMatrix(cofactors)
    for r in range(len(cofactors)):
        for c in range(len(cofactors)):
            try:
                cofactors[r][c] = cofactors[r][c]/determinant
            except ZeroDivisionError:
                print(ZERO_DIVISION)
                exit(-1)
    return cofactors


def division(matrix_a, matrix_b):
    result = [[0 for i in range(len(matrix_b[0]))] for j in range(len(matrix_a))]
    for i in range(len(matrix_a)):
        for j in range(len(getMatrixInverse(matrix_b)[0])):
            for k in range(len(getMatrixInverse(matrix_b))):
                result[i][j] += matrix_a[i][k] * getMatrixInverse(matrix_b)[k][j]
    return result


a = []
b = []
currentA = True

try:
    try:
        with open(const_matrix.INPUT, 'r') as input_file:
            for i in range(2):
                k = input_file.readline()
                while k != '\n':
                    temp = k.replace('\n', '').split(" ")
                    if currentA:
                        a.append([float(i) for i in temp if i.isdigit()])
                    else:
                        b.append([float(i) for i in temp if i.isdigit()])
                    k = input_file.readline()
                currentA = False
    except FileNotFoundError:
        print(FILE_NOT_FOUND_ERROR)

    with open(const_matrix.OUTPUT, 'w') as output_file:
        output_file.write("Addition: \n")
        for i in addition(a, b):
            output_file.write(str(i) + '\n')

        output_file.write("Subtraction: \n")
        for i in subtraction(a, b):
            output_file.write(str(i) + '\n')

        output_file.write("Multiplication: \n")
        for i in multiplication(a, b):
            output_file.write(str(i) + '\n')

        output_file.write("Division: \n")
        for i in division(a, b):
            output_file.write(str(i) + '\n')
except AttributeError:
    print(ATTRIBUTE_ERROR)


