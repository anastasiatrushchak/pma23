def read_matrix_from_file(filename):
    matrix = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                matrix.append(list(map(int, line.strip().split())))
    except FileNotFoundError:
        print(f"Error: File {filename} not found.")
    except ValueError:
        print(f"Error: Invalid data format in {filename}.")
    return matrix

def write_matrix_to_file(filename, matrix):
    try:
        with open(filename, 'a') as file:
            for row in matrix:
                file.write(' '.join(map(str, row)) + '\n')
            file.write('\n')
    except Exception as e:
        print(f"Error writing to file {filename}: {e}")

def add_matrices(A, B):
    try:
        return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]
    except IndexError:
        print("Not of the same size.")
        return []

def subtract_matrices(A, B):
    try:
        return [[A[i][j] - B[i][j] for j in range(len(A[0]))] for i in range(len(A))]
    except IndexError:
        print("Not of the same size.")
        return []

def multiply_matrices(A, B):
    try:
        return [[sum(A[i][k] * B[k][j] for k in range(len(A))) for j in range(len(B[0]))] for i in range(len(A))]
    except IndexError:
        print("Dimentions error")
        return []

def inverse_matrix_2x2(matrix):
    try:
        det = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
        if det == 0:
            raise ValueError("Matrix is singular and cannot be inverted.")
        return [[matrix[1][1]/det, -matrix[0][1]/det], [-matrix[1][0]/det, matrix[0][0]/det]]
    except IndexError:
        print("Not 2x2.")
        return []

def divide_matrices(A, B):
    inv_B = inverse_matrix_2x2(B)
    if not inv_B:
        print("Matrix B is not invertible.")
        return []
    return multiply_matrices(A, inv_B)

matrixA = read_matrix_from_file('matrixA.txt')
matrixB = read_matrix_from_file('matrixB.txt')

result_add = add_matrices(matrixA, matrixB)
result_subtract = subtract_matrices(matrixA, matrixB)
result_multiply = multiply_matrices(matrixA, matrixB)
result_divide = divide_matrices(matrixA, matrixB)

write_matrix_to_file('result.txt', result_add)
write_matrix_to_file('result.txt', result_subtract)
write_matrix_to_file('result.txt', result_multiply)
write_matrix_to_file('result.txt', result_divide) put
