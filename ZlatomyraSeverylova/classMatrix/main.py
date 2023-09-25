INPUT_MATRIX_A = 'input_matrix_a.txt'
INPUT_MATRIX_B = 'input_matrix_b.txt'
OUT_MATRIX = 'out_matrix.txt'

from class_matrix import Matrix
matrix_a  = Matrix.read(INPUT_MATRIX_A)
matrix_b  = Matrix.read(INPUT_MATRIX_B)
Matrix.write(OUT_MATRIX, 'Sum of matrix: ', matrix_a.__add__(matrix_b))
Matrix.write(OUT_MATRIX, 'Difference of matrix: ', matrix_a.__sub__(matrix_b))
Matrix.write(OUT_MATRIX, 'Multiplication of matrix: ', matrix_a.__mul__(matrix_b))
Matrix.write(OUT_MATRIX, 'Division of matrix: ', matrix_a.__truediv__(matrix_b))
