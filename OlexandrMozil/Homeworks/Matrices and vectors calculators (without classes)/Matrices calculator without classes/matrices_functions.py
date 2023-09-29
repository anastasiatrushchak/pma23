import exceptions as exc

def zero_matrix(size):
    return [[0 for _ in range(size)] for _ in range(size)]


def summ(matrix1, matrix2):
    summ = zero_matrix(len(matrix1))
    for i in range(len(matrix1)):
        for j in range(len(matrix1[0])):
            summ[i][j] = matrix1[i][j] + matrix2[i][j]
    return summ


def subtraction(matrix1, matrix2):
    subtr = zero_matrix(len(matrix1))
    for i in range(len(matrix1)):
        for j in range(len(matrix1[0])):
            subtr[i][j] = matrix1[i][j] - matrix2[i][j]
    return subtr


def multiplication(matrix1, matrix2):
    multiplication = zero_matrix(len(matrix1))
    for i in range(len(matrix1)):
        for j in range(len(matrix2[0])):
            for k in range(len(matrix2)):
                multiplication[i][j] += matrix1[i][k] * matrix2[k][j]
    return multiplication


def multiplication_by_number(matrix, number):
    number_multiplication = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            number_multiplication[i][j] = number * matrix[i][j]
    return number_multiplication


def get_matrix_minor(matrix, row, col):
    return [[matrix[i][j] for j in range(len(matrix[0])) if j != col] for i in range(len(matrix)) if i != row]


def get_determinant(matrix):
    n = len(matrix)
    if n == 1:
        return matrix[0][0]
    elif n == 2:
        return (matrix[0][0] * matrix[1][1]) - (matrix[0][1] * matrix[1][0])
    else:
        determinant = 0
        for col in range(n):
            minor = get_matrix_minor(matrix, 0, col)
            determinant += matrix[0][col] * ((-1) ** col) * get_determinant(minor)
        return determinant


def get_cofactor_matrix(matrix):
    n = len(matrix)
    cofactor_matrix = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            minor = get_matrix_minor(matrix, i, j)
            determinant = get_determinant(minor)
            cofactor_matrix[i][j] = ((-1) ** (i + j)) * determinant
    return cofactor_matrix


def transpose(matrix):
    transposed = [[0 for i in range(len(matrix))] for j in range(len(matrix[0]))]
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if i != j:
                transposed[i][j] = matrix[j][i]
            else:
                transposed[i][j] = matrix[i][j]
    return transposed


def division(matrix1, matrix2):
    try:
        prepared_matrix = get_cofactor_matrix(matrix2)
        prepared_matrix = transpose(prepared_matrix)
        prepared_matrix = multiplication_by_number(prepared_matrix, 1 / (get_determinant(matrix2)))
        return multiplication(matrix1, prepared_matrix)
    except ZeroDivisionError:
        print("Division by zero!")
        raise SystemExit



def matrix_to_string(matrix):
    matrix_strings = [' '.join(map(str, row)) for row in matrix]
    return '\n'.join(matrix_strings)