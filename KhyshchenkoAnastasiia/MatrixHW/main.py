def read_matrix(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        matrix = [[int(num) for num in line.split()] for line in lines]
    return matrix
def add_matrices(matrix1, matrix2):
    result = [[matrix1[i][j] + matrix2[i][j] for j in range(len(matrix1[0]))] for i in range(len(matrix1))]
    return result

def subtract_matrices(matrix1, matrix2):
    result = [[matrix1[i][j] - matrix2[i][j] for j in range(len(matrix1[0]))] for i in range(len(matrix1))]
    return result

def multiply_matrices(matrix1, matrix2):
    result = [[sum(matrix1[i][k] * matrix2[k][j] for k in range(len(matrix2))) for j in range(len(matrix2[0]))] for i in range(len(matrix1))]
    return result

def divide_matrices(matrix1, matrix2):
    result = [[matrix1[i][j] / matrix2[i][j] for j in range(len(matrix1[0]))] for i in range(len(matrix1))]
    return result
def write_matrix_to_file(result, filename):
    with open(filename, 'w') as file:
        for row in result:
            file.write(' '.join(map(str, row)) + '\n')
if __name__ == "__main__":
    matrix1 = read_matrix('matrix1.txt')
    matrix2 = read_matrix('matrix2.txt')

    result_addition = add_matrices(matrix1, matrix2)
    write_matrix_to_file(result_addition, 'result_addition.txt')

    result_subtraction = subtract_matrices(matrix1, matrix2)
    write_matrix_to_file(result_subtraction, 'result_subtraction.txt')

    result_multiplication = multiply_matrices(matrix1, matrix2)
    write_matrix_to_file(result_multiplication, 'result_multiplication.txt')

    result_division = divide_matrices(matrix1, matrix2)
    write_matrix_to_file(result_division, 'result_division.txt')
