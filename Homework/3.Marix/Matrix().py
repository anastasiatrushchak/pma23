def multiplication(matrix_first, matrix_second):
    matrix_multiplication = []
    for i in range(len(matrix_first)):
        row = []
        for j in range(len(matrix_second[0])):
            number = 0
            for k in range(max(len(matrix_first[0]), len(matrix_second))):
                number += float(matrix_first[i][k]) * float(matrix_second[k][j])
            row.append(round(number, 3))
        matrix_multiplication.append(row)
    return matrix_multiplication

MATRIX_FIRST_INPUT = 'matrix1.txt'
MATRIX_SECOND_INPUT = 'matrix2.txt'
MATRIX_RESULT = 'matrix_rez.txt'
mode = 'r'

matrix_first = []
matrix_second = []

try:
    with open(MATRIX_FIRST_INPUT, mode) as lines:
        lines = lines.readlines()

        for line in lines:
            row = [float(x) for x in line.split()]
            matrix_first.append(row)
except FileNotFoundError:
    print("File " + MATRIX_FIRST_INPUT + "no found")
    exit(-1)

try:
    with open(MATRIX_SECOND_INPUT, mode) as lines:
        lines = lines.readlines()

        for line in lines:
            row = [float(x) for x in line.split()]
            matrix_second.append(row)
except FileNotFoundError:
    print("File " + MATRIX_SECOND_INPUT + "no found")
    exit(-1)

try:
    matrix_multiplication = multiplication(matrix_first, matrix_second)

    with open(MATRIX_RESULT, 'w') as file:
        file.write("Multiplication:\n")
        for row in matrix_multiplication:
            file.write(str(row)+'\n')
except IndexError:
    print("The number of columns of the first matrix is not equal to the number of rows of the second matrix: " + str(len(matrix_first[0])) + '!=' + str(len(matrix_second)))



len_matrix_second = max(len(matrix_second),len(matrix_second[0]))
try:
    inverse_matrix_second = []
    if len_matrix_second == 1:
        inverse_matrix_second = [[1 / matrix_second[0][0]]]

    elif len_matrix_second == 2:
        det = matrix_second[0][0] * matrix_second[1][1] - matrix_second[0][1] * matrix_second[1][0]
        inverse_matrix_second = [[matrix_second[1][1] / det, -matrix_second[0][1] / det],
                [-matrix_second[1][0] / det, matrix_second[0][0] / det]]

    elif len_matrix_second == 3:
        det = (matrix_second[0][0] * ((matrix_second[1][1] * matrix_second[2][2]) - (matrix_second[1][2] * matrix_second[2][1])) -
                matrix_second[0][1] * ((matrix_second[1][0] * matrix_second[2][2]) - (matrix_second[1][2] * matrix_second[2][0])) +
                matrix_second[0][2] * ((matrix_second[1][0] * matrix_second[2][1]) - (matrix_second[1][1] * matrix_second[2][0])))

        inverse_matrix_second = [[0] * 3 for _ in range(3)]
        inverse_matrix_second[0][0] = (matrix_second[1][1] * matrix_second[2][2] - matrix_second[1][2] * matrix_second[2][1]) / det
        inverse_matrix_second[0][1] = (matrix_second[0][2] * matrix_second[2][1] - matrix_second[0][1] * matrix_second[2][2]) / det
        inverse_matrix_second[0][2] = (matrix_second[0][1] * matrix_second[1][2] - matrix_second[0][2] * matrix_second[1][1]) / det
        inverse_matrix_second[1][0] = (matrix_second[1][2] * matrix_second[2][0] - matrix_second[1][0] * matrix_second[2][2]) / det
        inverse_matrix_second[1][1] = (matrix_second[0][0] * matrix_second[2][2] - matrix_second[0][2] * matrix_second[2][0]) / det
        inverse_matrix_second[1][2] = (matrix_second[0][2] * matrix_second[1][0] - matrix_second[0][0] * matrix_second[1][2]) / det
        inverse_matrix_second[2][0] = (matrix_second[1][0] * matrix_second[2][1] - matrix_second[1][1] * matrix_second[2][0]) / det
        inverse_matrix_second[2][1] = (matrix_second[0][1] * matrix_second[2][0] - matrix_second[0][0] * matrix_second[2][1]) / det
        inverse_matrix_second[2][2] = (matrix_second[0][0] * matrix_second[1][1] - matrix_second[0][1] * matrix_second[1][0]) / det
    matrix_division = multiplication(matrix_first, inverse_matrix_second)

    with open(MATRIX_RESULT, 'a') as file:
        file.write("Division:\n")
        for row in matrix_division:
            file.write(str(row)+'\n')
except ZeroDivisionError:
    print("The matrix does not have an inverse because the determinant is zero.")
    exit(-1)
except IndexError:
    print("The number of columns of the first matrix is not equal to the number of rows of the second inverse matrix: " + str(len(matrix_first[0])) + '!=' + str(len(inverse_matrix_second)))
    exit(-1)


