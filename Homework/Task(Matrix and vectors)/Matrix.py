import numpy as np

def read_matrix(filename):
    with open(filename, 'r') as f:
        matrix = [[int(num) for num in line.split()] for line in f]
    return np.array(matrix)
def write_matrix(filename, matrix):
    with open(filename, 'w') as f:
        for row in matrix:
            f.write(' '.join(['{:0.5g}'.format(x) for x in row]) + '\n')
def matrix_calculator(A, B, operation):
    if operation == 'add':
        return np.add(A, B)
    elif operation == 'subtract':
        return np.subtract(A, B)
    elif operation == 'multiply':
        return np.dot(A, B)
    elif operation == 'divide':
        return np.dot(A, np.linalg.inv(B))
    else:
        return "Invalid operation"


MatrixA = read_matrix('matrix_A.txt')
MatrixB = read_matrix('matrix_B.txt')

operation = input("Enter operation (add, subtract, multiply, divide): ")
result = matrix_calculator(MatrixA, MatrixB, operation)

print("The result is:")
for row in result:
    print(' '.join(['{:0.5g}'.format(x) for x in row]))

write_matrix('result_matrix.txt', result)