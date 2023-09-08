import numpy as np

def matrix_from_file(filename):
    try:
        with open(filename, 'r') as f:
            matrix = [[int(num) for num in line.split()] for line in f]
        return np.array(matrix)
    except FileNotFoundError:
        return f"File '{filename}' not found"
    except ValueError as e:
        return f"Error reading matrix from '{filename}': {e}"

def matrix_to_file(matrix, filename):
    try:
        with open(filename, 'w') as f:
            for row in matrix:
                f.write(' '.join(['{:0.5g}'.format(x) for x in row]) + '\n')
    except Exception as e:
        return f"Error writing matrix to '{filename}': {e}"

def matrix_add(A, B):
    try:
        if A.shape != B.shape:
            raise ValueError("Matrix dimensions must be the same for addition.")
        return np.add(A, B)
    except ValueError as e:
        return f"ValueError: {e}"

def matrix_subtract(A, B):
    try:
        if A.shape != B.shape:
            raise ValueError("Matrix dimensions must be the same for subtraction.")
        return np.subtract(A, B)
    except ValueError as e:
        return f"ValueError: {e}"

def matrix_multiply(A, B):
    try:
        if A.shape[1] != B.shape[0]:
            raise ValueError("Number of columns in the first matrix must be equal to the number of rows in the second matrix for multiplication.")
        return np.dot(A, B)
    except ValueError as e:
        return f"ValueError: {e}"

def matrix_divide(A, B):
    try:
        if A.shape[1] != B.shape[0]:
            raise ValueError("Number of columns in the first matrix must be equal to the number of rows in the second matrix for division.")
        inverse_B = np.linalg.inv(B)
        return np.dot(A, inverse_B)
    except ValueError as e:
        return f"ValueError: {e}"
    except np.linalg.LinAlgError as e:
        return f"LinalgError: {e}"

MatrixA = matrix_from_file('matrix_A.txt')
MatrixB = matrix_from_file('matrix_B.txt')

if isinstance(MatrixA, str) or isinstance(MatrixB, str):
    print(MatrixA)
    print(MatrixB)
else:
    operation = input("Enter operation (add, subtract, multiply, divide): ")
    if operation == 'add':
        result = matrix_add(MatrixA, MatrixB)
    elif operation == 'subtract':
        result = matrix_subtract(MatrixA, MatrixB)
    elif operation == 'multiply':
        result = matrix_multiply(MatrixA, MatrixB)
    elif operation == 'divide':
        result = matrix_divide(MatrixA, MatrixB)
    else:
        result = "Invalid operation"

    print("The result is:")
    for row in result:
        print(' '.join(['{:0.5g}'.format(x) for x in row]))

    matrix_to_file(result, 'result_matrix.txt')
