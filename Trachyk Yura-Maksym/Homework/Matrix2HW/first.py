MATRIX_FIRST_INPUT = 'MatrixA.txt'
MATRIX_SECOND_INPUT = 'MatrixB.txt'
MATRIX_RESULT = 'output.txt'

matrix1 = []
matrix2 = []

try:
    with open(MATRIX_FIRST_INPUT, "r") as lines:
        lines = lines.readlines()

        for line in lines:
            row = [float(x) for x in line.split()]
            matrix1.append(row)
except FileNotFoundError:
    print("File " + MATRIX_FIRST_INPUT + " not found")
    exit(-1)

try:
    with open(MATRIX_SECOND_INPUT, "r") as lines:
        lines = lines.readlines()
        for line in lines:
            row = [float(x) for x in line.split()]
            matrix2.append(row)

except FileNotFoundError:
    print("File " + MATRIX_SECOND_INPUT + " not found")
    exit(-1)

def multiply_matrices_and_write_to_file(matrix_1, matrix_2, result_file):
    # Check if the number of columns in matrix 1 is equal to the number of rows in matrix 2
    if len(matrix_1[0]) != len(matrix_2):
        return "Matrix multiplication is not possible. Dimensions do not match."

    # Perform matrix multiplication and write it to the specified file
    with open(result_file, 'w') as file:
        result_matrix = [[0 for _ in range(len(matrix_2[0]))] for _ in range(len(matrix_1))]
        for i in range(len(matrix_1)):
            for j in range(len(matrix_2[0])):
                for k in range(len(matrix_2)):
                    result_matrix[i][j] += matrix_1[i][k] * matrix_2[k][j]
        file.write("Matrix A * Matrix B:\n")
        for row in result_matrix:
            file.write(' '.join(map(str, row)) + '\n')
        file.write("\n")

    # Check if the number of columns in matrix 2 is equal to the number of rows in matrix 1
    if len(matrix_2[0]) != len(matrix_1):
        return "Matrix division is not possible. Dimensions do not match."

    # Perform matrix division and write it to the specified file
    with open(result_file, 'a') as file:
        result_matrix_inverse = [[0 for _ in range(len(matrix_1[0]))] for _ in range(len(matrix_2))]
        for i in range(len(matrix_2)):
            for j in range(len(matrix_1[0])):
                for k in range(len(matrix_1)):
                    try:
                        result_matrix_inverse[i][j] += matrix_2[i][k] / matrix_1[k][j]
                    except ZeroDivisionError:
                        print("Cannot be divided by 0")
                        exit(-1)
        file.write("Matrix B / Matrix A:\n")
        for row in result_matrix_inverse:
            file.write(' '.join(map(str, row)) + '\n')

    return "Matrix multiplication and division results have been written to the file."

# Example usage:
result_message = multiply_matrices_and_write_to_file(matrix1, matrix2, MATRIX_RESULT)
print(result_message)






