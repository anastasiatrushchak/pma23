from RostyslavPasternak.Homework.Homework_1.Exception import InvalidSize, InvalidMatrixInverse
def str_matrix(matrix):
    matrix_str = ""
    for row in matrix:
        matrix_str += "\t".join(map(str, row)) + "\n"
    return matrix_str

def add(first_matrix, second_matrix):
    first_matrix_row = len(first_matrix)
    first_matrix_column = len(first_matrix[0])
    second_matrix_row = len(second_matrix)
    second_matrix_column = len(second_matrix[0])
    if first_matrix_row != second_matrix_row | first_matrix_column != second_matrix_column:
        raise InvalidSize()
    result = [[0 for _ in range(first_matrix_row)] for _ in range(first_matrix_row)]
    for i in range(0, first_matrix_column):
        for j in range(0, first_matrix_row):
            result[i][j] = first_matrix[i][j] + second_matrix[i][j]
    return result


def sub(first_matrix, second_matrix):
    first_matrix_row = len(first_matrix)
    first_matrix_column = len(first_matrix[0])
    second_matrix_row = len(second_matrix)
    second_matrix_column = len(second_matrix[0])
    if first_matrix_row != second_matrix_row | first_matrix_column != second_matrix_column:
        raise InvalidSize()
    result = [[0 for _ in range(first_matrix_column)] for _ in range(first_matrix_row)]
    for i in range(0, first_matrix_column):
        for j in range(0, first_matrix_row):
            result[i][j] = first_matrix[i][j] - second_matrix[i][j]
    return result
def mul(first_matrix, second_matrix):
    first_matrix_row = len(first_matrix)
    first_matrix_column = len(first_matrix[0])
    second_matrix_row = len(second_matrix)
    second_matrix_column = len(second_matrix[0])
    if first_matrix_row != second_matrix_column | first_matrix_column != second_matrix_row:
        raise InvalidSize()
    result = [[0 for _ in range(first_matrix_column)] for _ in range(first_matrix_row)]
    for i in range(first_matrix_column):
        for j in range(second_matrix_column):
            result[i][j] = sum(first_matrix[i][k] * second_matrix[k][j] for k in range(first_matrix_column))
    return result
def div(first_matrix, second_matrix):
    return mul(first_matrix, inverse(second_matrix))
def inverse(matrix):
    row = len(first_matrix)
    column = len(first_matrix[0])
    if row != column:
         raise InvalidSize()

    identity_matrix = [[0] * column for _ in range(row)]
    for i in range(row):
        identity_matrix[i][i] = 1

    matrix_copy = [row[:] for row in matrix]

    for i in range(row):
        pivot = matrix_copy[i][i]
        if pivot == 0:
            raise InvalidMatrixInverse()
        for j in range(column):
            matrix_copy[i][j] /= pivot
            identity_matrix[i][j] /= pivot

        for k in range(row):
            if k != i:
                factor = matrix_copy[k][i]
                for j in range(column):
                    matrix_copy[k][j] -= factor * matrix_copy[i][j]
                    identity_matrix[k][j] -= factor * identity_matrix[i][j]
    return identity_matrix
def str_to_file(matrix,file_name="result.txt"):
    with open(file_name, 'w') as writeFile:
        writeFile.write(str_matrix(matrix))

with open("matrix1.txt", 'r') as file:
    lines = file.readlines()
first_matrix = []

for line in lines:
    matrix_temp = [int(element) for element in line.split(" ")]
    first_matrix.append(matrix_temp)
print(str_matrix(first_matrix))
with open("matrix2.txt", 'r') as file:
    lines = file.readlines()
second_matrix = []

for line in lines:
    matrix_temp = [int(element) for element in line.split(" ")]
    second_matrix.append(matrix_temp)
print(str_matrix(second_matrix))
while True:
    try:
        operator = int(input("1. Add\n2. Subtraction\n3. Multiplication\n4. Division\n5. Inverse\n0. Cancel\n"))
        if operator == 1:
            result = add(first_matrix, second_matrix)
        elif operator == 2:
            result = sub(first_matrix, second_matrix)
        elif operator == 3:
            result = mul(first_matrix, second_matrix)
        elif operator == 4:
            result = div(first_matrix, second_matrix)
        elif operator == 5:
            result = inverse(first_matrix)
        else:
            break
    except InvalidSize as e:
        print(e)
    except InvalidMatrixInverse as e:
        print(e)
    else:
        print(str_matrix(result))
        str_to_file(result)