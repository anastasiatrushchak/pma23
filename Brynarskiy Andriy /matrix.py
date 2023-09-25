# Функція для читання матриці з файлу
def read_matrix(file_name):
    matrix = []
    with open(file_name, 'r') as file:
        for line in file:
            row = [float(x) for x in line.strip().split(',')]
            matrix.append(row)
    return matrix

# Функція для запису матриці у файл
def write_matrix(matrix, file_name):
    with open(file_name, 'w') as file:
        for row in matrix:
            file.write(' '.join(map(str, row)) + '\n')

# Функція для додавання матриць
def add_matrices(matrix1, matrix2):
    result = []
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        raise ValueError("Розміри матриць не співпадають")
    for i in range(len(matrix1)):
        row = [matrix1[i][j] + matrix2[i][j] for j in range(len(matrix1[0]))]
        result.append(row)
    return result

# Функція для віднімання матриць
def subtract_matrices(matrix1, matrix2):
    result = []
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        raise ValueError("Розміри матриць не співпадають")
    for i in range(len(matrix1)):
        row = [matrix1[i][j] - matrix2[i][j] for j in range(len(matrix1[0]))]
        result.append(row)
    return result

# Функція для множення матриць
def multiply_matrices(matrix1, matrix2):
    if len(matrix1[0]) != len(matrix2):
        raise ValueError("Кількість стовпців першої матриці не дорівнює кількості рядків другої матриці")
    result = [[0 for _ in range(len(matrix2[0]))] for _ in range(len(matrix1))]
    for i in range(len(matrix1)):
        for j in range(len(matrix2[0])):
            for k in range(len(matrix2)):
                result[i][j] += matrix1[i][k] * matrix2[k][j]
    return result

#Виконуємо транспонацію матриці
def transpose_matrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    transposed = [[0 for _ in range(rows)] for _ in range(cols)]

    for i in range(rows):
        for j in range(cols):
            transposed[j][i] = matrix[i][j]

    return transposed

# Зчитуємо матриці з файлів
matrix_A = read_matrix('matrix_A.txt')
matrix_B = read_matrix('matrix_B.txt')
transpose_matrix_B = transpose_matrix(matrix_B)

# Виконуємо операції
result_add = add_matrices(matrix_A, matrix_B)
result_subtract = subtract_matrices(matrix_A, matrix_B)
result_multiply = multiply_matrices(matrix_A, matrix_B)
result_division = multiply_matrices(matrix_A,transpose_matrix_B)

# Записуємо результати у файли
write_matrix(result_add, 'result_add.txt')
write_matrix(result_subtract, 'result_subtract.txt')
write_matrix(result_multiply, 'result_multiply.txt')
write_matrix(result_division, 'result_division.txt')
