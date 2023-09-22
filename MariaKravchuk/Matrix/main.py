def input_matrix_file(name_file):
    matrix = []
    try:
        with open(name_file, 'r') as file:
            for line in file:
                row = [int(x) for x in line.strip().split()]
                matrix.append(row)
    except FileNotFoundError:
        print(f"Error: File '{name_file}' not found.")
        return None

    return matrix  

def result_in_file(matrix, file_name, label):
    with open(file_name, 'a') as file:
        file.write(label + ":\n")
        for row in matrix:
            file.write(' '.join(map(str, row)) + '\n')
        file.write('\n')

def add_matrices(first_matrix, second_matrix):
    if len(first_matrix) != len(second_matrix) or len(first_matrix[0]) != len(second_matrix[0]):
        return None
    result = []
    for i in range(len(first_matrix)):
        row = []
        for j in range(len(first_matrix[0])):
            row.append(first_matrix[i][j] + second_matrix[i][j])
        result.append(row)
    return result

def sub_matrices(first_matrix, second_matrix):
    if len(first_matrix) != len(second_matrix) or len(first_matrix[0]) != len(second_matrix[0]):
        return None
    result = []
    for i in range(len(first_matrix)):
        row = []
        for j in range(len(first_matrix[0])):
            row.append(first_matrix[i][j] - second_matrix[i][j])
        result.append(row)
    return result

def multiply_matrices(first_matrix, second_matrix):
    m = len(first_matrix)
    n = len(first_matrix[0])
    p = len(second_matrix[0])

    result = [[0 for _ in range(p)] for _ in range(m)]

    for i in range(m):
        for j in range(p):
            for k in range(n):
                result[i][j] += first_matrix[i][k] * second_matrix[k][j]

    return result

def inverse_matrix(matrix):
    n = len(matrix)

    augmented_matrix = [row + [1 if i == j else 0 for j in range(n)] for i, row in enumerate(matrix)]

    for i in range(n):
        divisor = augmented_matrix[i][i]
        for j in range(2 * n):
            augmented_matrix[i][j] /= divisor

        for k in range(n):
            if k != i:
                factor = augmented_matrix[k][i]
                for j in range(2 * n):
                    augmented_matrix[k][j] -= factor * augmented_matrix[i][j]

    inverse = [row[n:] for row in augmented_matrix]

    return inverse

def divide_matrices(first_matrix, second_matrix):
    if len(first_matrix[0]) != len(second_matrix):
        return None

    if all(all(element == 0 for element in row) for row in second_matrix):
        print("Error: Division by zero matrix is not allowed.")
        return None

    result = multiply_matrices(first_matrix, inverse_matrix(second_matrix))

    return result

first_matrix = input_matrix_file('matrix1.txt')
second_matrix = input_matrix_file('matrix2.txt')

if first_matrix is not None and second_matrix is not None:
    with open("output.txt", 'w') as file:
        file.write("")

    result_in_file(first_matrix, "output.txt", "Matrix 1")
    result_in_file(second_matrix, "output.txt", "Matrix 2")

    result_matrix = multiply_matrices(first_matrix, second_matrix)
    if result_matrix is not None:
        result_in_file(result_matrix, "output.txt", "Multiplication")
    else:
        print("Multiplication is not possible.")

    add_matrix = add_matrices(first_matrix, second_matrix)
    if add_matrix is not None:
        result_in_file(add_matrix, "output.txt", "Addition")
    else:
        print("Addition is not possible.")

    sub_matrix = sub_matrices(first_matrix, second_matrix)
    if sub_matrix is not None:
        result_in_file(sub_matrix, "output.txt", "Subtraction")
    else:
        print("Subtraction is not possible.")

    div_matrix = divide_matrices(first_matrix, second_matrix)
    if div_matrix is not None:
        result_in_file(div_matrix, "output.txt", "Division")
    else:
        print("Division is not possible.")
else:
    print("Matrix loading failed. Check the input files.")
