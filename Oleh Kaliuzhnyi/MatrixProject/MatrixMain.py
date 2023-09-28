MATRIX_ONE_FILE = "MatrixOne.txt"
MATRIX_TWO_FILE = "MatrixTwo.txt"


def set_matrix(file_name, matrix):
    with open(file_name) as file:
        for i in range(3):
            line = file.readline()
            matrix.append(line.split())
            matrix[i] = [int(j) for j in matrix[i] if j.isdigit]

def add_Matrix_To_File(resultText, matrix):
    with open(resultText, "w") as file:
        for i in range(3):
            file.write(str(matrix[i]))
            file.write('\n')


def sum_matrix(file_name_one, file_name_two):
    matrix_one = []
    matrix_two = []
    matrix_result = []
    set_matrix(file_name_one, matrix_one)
    set_matrix(file_name_two, matrix_two)
    for i in range(3):
        array = []
        for j in range(3):
            array.append(matrix_one[i][j]+matrix_two[i][j])
        matrix_result.append(array)
    add_Matrix_To_File("SumResult.txt", matrix_result)


def subtract_matrix(file_name_one, file_name_two):
    matrix_one = []
    matrix_two = []
    matrix_result = []
    set_matrix(file_name_one, matrix_one)
    set_matrix(file_name_two, matrix_two)
    for i in range(3):
        array = []
        for j in range(3):
            array.append(matrix_one[i][j] - matrix_two[i][j])
        matrix_result.append(array)
    add_Matrix_To_File("SubtractionResult.txt", matrix_result)


def multiply_matrix(file_name_one, file_name_two):
    matrix_one = []
    matrix_two = []
    matrix_result = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    set_matrix(file_name_one, matrix_one)
    set_matrix(file_name_two, matrix_two)
    for i in range(3):
        for j in range(3):
            for k in range(3):
                matrix_result[i][j] += matrix_one[i][k] * matrix_two[k][j]
    add_Matrix_To_File("MultiplyResult.txt", matrix_result)


def get_det(matrix):
    det = 0
    size = len(matrix)
    if size == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    elif size == 3:
        for i in range(3):
            det += matrix[0][i] * (matrix[1][(i + 1) % 3] * matrix[2][(i + 2) % 3] - matrix[1][(i + 2) % 3] * matrix[2][(i + 1) % 3])
        return det
    elif size > 3:
        raise Exception("Error! Matrix size is >3")


def divide_matrix(file_name_one, file_name_two):
    matrix_one = []
    matrix_two = []
    matrix_result = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    set_matrix(file_name_one, matrix_one)
    set_matrix(file_name_two, matrix_two)
    try:
        n = len(matrix_two)
        det = get_det(matrix_two)
        if det == 0:
            raise Exception("Error! Det == 0! Dividing is impossible")
        adj_matrix = []
        for j in range(n):
            adj_row = []
            for i in range(n):
                submatrix = [row[:j] + row[j + 1:] for row in (matrix_two[:i] + matrix_two[i + 1:])]
                cofactor = get_det(submatrix) * (-1) ** (i + j)
                adj_row.append(cofactor)
            adj_matrix.append(adj_row)
        for i in range(3):
            for j in range(3):
                for k in range(3):
                    matrix_result[i][j] += matrix_one[i][k] * adj_matrix[k][j]
        add_Matrix_To_File("DividingResult.txt", matrix_result)
    except Exception as err:
        print(err)


divide_matrix(MATRIX_ONE_FILE, MATRIX_TWO_FILE)