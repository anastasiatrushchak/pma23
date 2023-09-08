import constants

matrix_a = []
matrix_b = []

with open(constants.INPUT_FILE, 'r') as file:
    new_matrix = False
    lines = file.readlines()
    for line in lines:
        if line == '\n':
            new_matrix = True
            continue
        if new_matrix:
            elements = line.strip().split(constants.SEPARATOR)
            row = [float(element) for element in elements]
            matrix_b.append(row)
        else:
            elements = line.strip().split(constants.SEPARATOR)
            row = [float(element) for element in elements]
            matrix_a.append(row)


def add(matrix_a, matrix_b):
    result = []
    for i in range(len(matrix_a)):
        result.append([])
        for j in range(len(matrix_a[0])):
            result[i].append(matrix_a[i][j] + matrix_b[i][j])
    with open(constants.OUTPUT_FILE, 'w') as file:
        file.write(str(result))


def subtract(matrix_a, matrix_b):
    result = []
    for i in range(len(matrix_a)):
        result.append([])
        for j in range(len(matrix_a[0])):
            result[i].append(matrix_a[i][j] - matrix_b[i][j])
    with open(constants.OUTPUT_FILE, 'w') as file:
        file.write(str(result))


def multiply(matrix_a, matrix_b):
    result = []
    for i in range(len(matrix_a)):
        result.append([])
        for j in range(len(matrix_a[0])):
            result[i].append(0)
            for k in range(len(matrix_b)):
                result[i][j] += matrix_a[i][k] * matrix_b[k][j]
    with open(constants.OUTPUT_FILE, 'w') as file:
        file.write(str(result))
    return result


def divide(matrix_a, matrix_b):
    transposed = [
        [matrix_b[1][1], -matrix_b[1][0]],
        [-matrix_b[0][1], matrix_b[0][0]]
    ]
    det = matrix_b[0][0] * matrix_b[1][1] - matrix_b[0][1] * matrix_b[1][0]
    inverse = []
    for i in range(len(transposed)):
        inverse.append([])
        for j in range(len(transposed[0])):
            inverse[i].append(transposed[j][i] / det)
    print(inverse)
    with open(constants.OUTPUT_FILE, 'w') as file:
        file.write(str(multiply(matrix_a, inverse)))




print(matrix_a)
print(matrix_b)

print("Choose operation(+,-,*,/):", end=' ')

match input():
    case '+':
        add(matrix_a, matrix_b)
    case '-':
        subtract(matrix_a, matrix_b)
    case '*':
        multiply(matrix_a, matrix_b)
    case '/':
        divide(matrix_a, matrix_b)
