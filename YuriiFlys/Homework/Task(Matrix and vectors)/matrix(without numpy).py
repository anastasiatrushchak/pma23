import sys


def read_matrix_from_file(file_path):
    matrix = []
    try:
        with open(file_path, 'r') as file:
            for line in file:
                row = [int(x) for x in line.strip().split()]
                matrix.append(row)
    except FileNotFoundError:
        print("Error reading file", file_path)
        sys.exit(0)
    return matrix


def matrix_to_file(matrix, filename):
    try:
        with open(filename, 'w') as f:
            for row in matrix:
                f.write(' '.join(['{:0.5g}'.format(x) for x in row]) + '\n')
    except Exception as e:
        return f"Error writing matrix to '{filename}': {e}"


def det2(A):
    return A[0][0] * A[1][1] - A[0][1] * A[1][0]


def inv2(A):
    d = det2(A)
    return [[A[1][1] / d, -A[0][1] / d], [-A[1][0] / d, A[0][0] / d]]


def det3(B):
    ret = 0
    for i in range(3):
        pos = 1
        neg = 1
        for j in range(3):
            pos *= B[j][(i + j) % 3]
            neg *= B[j][(i - j) % 3]
        ret += (pos - neg)

    return ret


def inv3(B):
    ret = [3 * [None] for _i in range(3)]
    det = det3(B)
    for i in range(3):
        for j in range(3):
            adj = [[n for ii, n in enumerate(row) if ii != i]
                   for jj, row in enumerate(B) if jj != j]
            d = det2(adj)
            sgn = (-1) ** (i + j)
            ret[i][j] = sgn * d / det
    return ret


def add_matrices(matrix_a, matrix_b):
    if len(matrix_a) != len(matrix_b) or len(matrix_a[0]) != len(matrix_b[0]):
        raise ValueError("Matrix dimensions do not match")

    result = [[0] * len(matrix_a[0]) for _ in range(len(matrix_a))]
    for i in range(len(matrix_a)):
        for j in range(len(matrix_a[0])):
            result[i][j] = matrix_a[i][j] + matrix_b[i][j]
    return result


def subtract_matrices(matrix_a, matrix_b):
    if len(matrix_a) != len(matrix_b) or len(matrix_a[0]) != len(matrix_b[0]):
        raise ValueError("Matrix dimensions do not match")

    result = []
    for i in range(len(matrix_a)):
        row = []
        for j in range(len(matrix_a[0])):
            row.append(matrix_a[i][j] - matrix_b[i][j])
        result.append(row)
    return result



def multiply_matrices(matrix_a, matrix_b):
    if len(matrix_a[0]) != len(matrix_b):
        raise ValueError("Invalid matrix dimensions for multiplication")

    result = []  # Ініціалізуємо порожній список для результату
    for i in range(len(matrix_a)):
        row = []  # Ініціалізуємо порожній рядок для кожного рядка результату
        for j in range(len(matrix_b[0])):
            sum_product = 0
            for k in range(len(matrix_a[0])):
                sum_product += matrix_a[i][k] * matrix_b[k][j]
            row.append(sum_product)  # Додаємо суму до рядка
        result.append(row)  # Додаємо рядок до результату
    return result



def inverse(matrix_a, matrix_b):
    if len(matrix_a) != len(matrix_a[0]) or len(matrix_b) != len(matrix_b[0]):
        raise ValueError("Invalid matrix dimensions for inversion")

    if len(matrix_a) == 2 and len(matrix_b) == 2:
        det = det2(matrix_b)
        if det == 0:
            raise ValueError("matrix_b is singular; cannot be inverted")
        inv = inv2(matrix_b)
        return inv

    elif len(matrix_a) == 3 and len(matrix_b) == 3:
        det = det3(matrix_b)
        if det == 0:
            raise ValueError("matrix_b is singular; cannot be inverted")
        inv = inv3(matrix_b)
        return inv
    else:
        raise ValueError("Unsupported matrix dimensions")


def divide_matrices(matrix_a, matrix_b):
    result = None
    try:
        # Check if matrix_b is a square matrix
        if len(matrix_b) != len(matrix_b[0]):
            raise ValueError("matrix_b must be a square matrix for inversion")

        # Check if the dimensions of matrix_a and matrix_b are compatible for multiplication
        if len(matrix_a[0]) != len(matrix_b):
            raise ValueError("Invalid matrix dimensions for division")

        # Compute the inverse of matrix_b
        if len(matrix_b) == 2:
            det = det2(matrix_b)
            if det == 0:
                raise ValueError("matrix_b is singular; cannot be inverted")
            inv = inv2(matrix_b)
        elif len(matrix_b) == 3:
            det = det3(matrix_b)
            if det == 0:
                raise ValueError("matrix_b is singular; cannot be inverted")
            inv = inv3(matrix_b)
        else:
            raise ValueError("Unsupported matrix dimensions")

        # Multiply matrix_a by the inverse of matrix_b
        result = multiply_matrices(matrix_a, inv)
    except Exception as e:
        print(f"Error performing division: {e}")
    return result


MatrixA = read_matrix_from_file('matrix_A.txt')
MatrixB = read_matrix_from_file('matrix_B.txt')

result = None

operation = input("Enter operation (add, subtract, multiply, divide): ")
try:
    if operation == 'add':
        result = add_matrices(MatrixA, MatrixB)
    elif operation == 'subtract':
        result = subtract_matrices(MatrixA, MatrixB)
    elif operation == 'multiply':
        result = multiply_matrices(MatrixA, MatrixB)
    elif operation == 'divide':
        result = divide_matrices(MatrixA, MatrixB)
    else:
        raise ValueError("Invalid operation")
except ValueError as e:
    print(f"Error performing operation: {e}")

try:
    if result is not None:
        print("Result:")
        for row in result:
            print(' '.join(['{:0.5g}'.format(x) for x in row]))
        matrix_to_file(result, 'result_4matrix.txt')
except Exception as e:
    print(f"Error writing matrix to file: {e}")


