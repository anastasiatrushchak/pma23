import numpy as np
try:
    with open('matr.input.txt', 'r') as f:
        n = int(f.readline())
        array = []
        for i in range(n):
            array.append(f.readline().split())
        array = [list(map(int, i)) for i in array]

        m = int(f.readline())
        array2 = []
        for i in range(m):
            array2.append(f.readline().split())
        array2 = [list(map(int, i)) for i in array2]

except FileNotFoundError:
    print("Error no file")
    exit(-1)
def matrix_mult(A, B):
    rows_A, cols_A = len(A), len(A[0])
    rows_B, cols_B = len(B), len(B[0])
    c = [[0 for _ in range(cols_B)] for _ in range(rows_A)]
    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                try:
                    c[i][j] += A[i][k] * B[k][j]
                except IndexError:
                    print("list index out of range")
    return c




print("Multiplication of two matrix:")
mult = matrix_mult(array, array2)
print(mult)

print("Addition of two matrix:")
result_add = [[array[i][j] + array2[i][j] for j in range(len(array[0]))] for i in range(len(array))]

for r in result_add:
    print(r)

print("Subtraction of two matrix:")
subtraction = [[array[i][j] - array2[i][j] for j in range(len(array[0]))] for i in range(len(array))]
print(subtraction)

print("Division of two matrix:")
# division = np.divide(array, array2)
# print(division)

# result = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
# for i in range(len(array)):
#     for j in range(len(array[0])):
#         result[i][j] = array[i][j] // array2[i][j]
#
# for r in result:
#     print(r)

def matrix_inverse(matrix):
    a, b, c = matrix[0]
    d, e, f = matrix[1]
    g, h, i = matrix[2]

    det = a * (e * i - f * h) - b * (d * i - f * g) + c * (d * h - e * g)

    # if det == 0:
    #     raise ValueError("Error, Determinant = 0")

    inv_det = 1 / det
    inv_matrix = [
        [(e * i - f * h) * inv_det, (c * h - b * i) * inv_det, (b * f - c * e) * inv_det],
        [(f * g - d * i) * inv_det, (a * i - c * g) * inv_det, (c * d - a * f) * inv_det],
        [(d * h - e * g) * inv_det, (g * b - a * h) * inv_det, (a * e - b * d) * inv_det]
    ]
    return inv_matrix


def matrix_divide(A, B):

    inverse_B = matrix_inverse(B)
    result = matrix_mult(A, inverse_B)
    return result

division=0
try:
    division = matrix_divide(array, array2)
    print(division)
except ZeroDivisionError as e:
    print("Error, determinant =0")
# print(array)
# print(matrix_mult(division, array2))


with open("matr.output.txt", 'w') as file:
    file.write("Multiplication:" + str(mult)+"\n")
    file.write("Addition:" + str(result_add)+"\n")
    file.write("Subtraction:" + str(subtraction)+"\n")
    file.write("Division:" + str(division)+"\n")


