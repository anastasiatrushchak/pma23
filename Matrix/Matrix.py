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


def add_matrices(matrix1, matrix2):
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        raise ValueError("Матриці мають бути однакового розміру для додавання")

    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix1[0])):
            row.append(matrix1[i][j] + matrix2[i][j])
        result.append(row)

    return result


def subtract_matrices(matrix1, matrix2):
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        raise ValueError("Матриці мають бути однакового розміру для віднімання")

    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix1[0])):
            row.append(matrix1[i][j] - matrix2[i][j])
        result.append(row)

    return result


def multiply_matrices(matrix1, matrix2):
    if len(matrix1[0]) != len(matrix2):
        raise ValueError("Кількість стовпців першої матриці повинна дорівнювати кількості рядків другої матриці")

    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix2[0])):
            value = 0
            for k in range(len(matrix2)):
                value += matrix1[i][k] * matrix2[k][j]
            row.append(value)
        result.append(row)

    return result


def inverse_matrix(matrix):
    if len(matrix) != len(matrix[0]):
        raise ValueError("Матриця повинна бути квадратною для знаходження оберненої матриці")

    n = len(matrix)

    identity_matrix = [[0] * n for _ in range(n)]
    for i in range(n):
        identity_matrix[i][i] = 1

    # Реалізація методу Гаусса-Джордана для знаходження оберненої матриці
    for col in range(n):
        # Пошук головного елемента в стовпці
        max_row = col
        for row in range(col + 1, n):
            if abs(matrix[row][col]) > abs(matrix[max_row][col]):
                max_row = row

        # Обмін рядків для забезпечення ненульового головного елемента
        matrix[col], matrix[max_row] = matrix[max_row], matrix[col]
        identity_matrix[col], identity_matrix[max_row] = identity_matrix[max_row], identity_matrix[col]

        # Ділення рядка на головний елемент, щоб зробити його рівним 1
        pivot = matrix[col][col]
        for j in range(n):
            matrix[col][j] /= pivot
            identity_matrix[col][j] /= pivot

        # Відняти інші рядки від поточного рядка, щоб зробити всі інші елементи в стовпці рівними 0
        for i in range(n):
            if i != col:
                factor = matrix[i][col]
                for j in range(n):
                    matrix[i][j] -= factor * matrix[col][j]
                    identity_matrix[i][j] -= factor * identity_matrix[col][j]

    return identity_matrix


file_exists("inputM.txt")
file_exists("inputM2.txt")
file_exists("outputM.txt")

X = read_matrix('inputM.txt')
Y = read_matrix('inputM2.txt')

result_add = add_matrices(X, Y)

with open('outputM.txt', 'a') as f:
    print("add:", file=f)
    for r in result_add:
        print(r, file=f)

result_sub = subtract_matrices(X, Y)

with open('outputM.txt', 'a') as f:
    print("sub:", file=f)
    for r in result_sub:
        print(r, file=f)

result_mult = multiply_matrices(X, Y)

with open('outputM.txt', 'a') as f:
    print("mult:", file=f)
    for r in result_mult:
        print(r, file=f)

inverse_matrix = inverse_matrix(Y)
print(inverse_matrix)
result_div = multiply_matrices(X, inverse_matrix)

with open('outputM.txt', 'a') as f:
    print("div:", file=f)
    for r in result_div:
        print(r, file=f)
