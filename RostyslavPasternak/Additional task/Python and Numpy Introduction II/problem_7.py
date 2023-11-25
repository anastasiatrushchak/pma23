import numpy as np
def row_stochastic_matrix(matrix):
    matrix = np.array(matrix)
    row_sums = np.sum(matrix, axis=1, keepdims=True)
    row_stochastic_matrix = matrix / row_sums
    return row_stochastic_matrix
def column_stochastic_matrix(matrix):
    matrix = np.array(matrix)
    return row_stochastic_matrix(matrix.T).T

matrix = [[3, 4, 5],
          [3, 4, 3],
          [4, 2, 2]]

result = row_stochastic_matrix(matrix)
print(result)
result = column_stochastic_matrix(matrix)
print(result)
