def multiply_matrices(matrix_a, matrix_b):
    result = [[0, 0], [0, 0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                result[i][j] += matrix_a[i][k] * matrix_b[k][j]
    return result
def add_matrices(matrix_a, matrix_b):
    result = [[0, 0], [0, 0]]
    for i in range(2):
        for j in range(2):
            result[i][j] = matrix_a[i][j] + matrix_b[i][j]
    return result

def subtract_matrices(matrix_a, matrix_b):
    result = [[0, 0], [0, 0]]
    for i in range(2):
        for j in range(2):
            result[i][j] = matrix_a[i][j] - matrix_b[i][j]
    return result


def inverse_matrix(matrix):
    det = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    if det == 0:
        raise ValueError("= 0.")

    inverse_det = 1.0 / det
    result = [[0, 0], [0, 0]]

    for i in range(2):
        for j in range(2):
            result[i][j] = matrix[1 - i][1 - j] * inverse_det
    return result


def divide_matrices(matrix_a, matrix_b):
    inverse_b = inverse_matrix(matrix_b)
    result = multiply_matrices(matrix_a, inverse_b)
    return result

try:
    with open("input.txt", "r") as file:
        lines = file.readlines()

    matrix_a = []
    matrix_b = []

    for i in range(2):
        row = [int(x) for x in lines[i].strip().split()]
        matrix_a.append(row)

    for i in range(3, 5):
        row = [int(x) for x in lines[i].strip().split()]
        matrix_b.append(row)
except FileNotFoundError:
    print("file not found")

result_addition = add_matrices(matrix_a, matrix_b)
result_subtraction = subtract_matrices(matrix_a, matrix_b)
result_multiplication = multiply_matrices(matrix_a, matrix_b)
result_division = divide_matrices(matrix_a, matrix_b)

with open("output.txt", "w") as file:
    file.write("addition:\n")
    for row in result_addition:
        file.write(" ".join(map(str, row)) + "\n")

    file.write("\nsubtraction:\n")
    for row in result_subtraction:
        file.write(" ".join(map(str, row)) + "\n")

    file.write("\nmultiplication:\n")
    for row in result_multiplication:
        file.write(" ".join(map(str, row)) + "\n")

    file.write("\ndivision:\n")
    for row in result_division:
        file.write(" ".join(map(str, row)) + "\n")

