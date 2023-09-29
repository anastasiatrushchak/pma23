class Matrix:
    def __init__(self, filename):
        self.matrix = []
        self.filename = filename

    def load_matrix(self):
        try:
            with open(self.filename, 'r') as matrix_file:
                for line in matrix_file:
                    row = [int(x) for x in line.strip().split()]
                    self.matrix.append(row)
        except Exception as e:
            print("Error:", e)

    def __len__(self):
        return len(self.matrix)

    def __add__(self, other):
        result_matrix = []
        for i in range((len(self))):
            row = []
            for j in range(len(self.matrix[0])):
                row.append(self.matrix[i][j] + other[i][j])
            result_matrix.append(row)
        return result_matrix

    def __sub__(self, other):
        result_matrix = []
        for i in range(len(self)):
            row = []
            for j in range(len(self.matrix[0])):
                row.append(self.matrix[i][j] - other[i][j])
            result_matrix.append(row)
        return result_matrix

    def __mul__(self, other):
        result_matrix = []
        for i in range(len(self)):
            row = []
            for j in range(len(other[0])):
                mult = 0
                for k in range(len(other)):
                    mult += self.matrix[i][k] * other[k][j]
                row.append(mult)
            result_matrix.append(row)
        return result_matrix

    def determinant(self, matrix):
        size = len(matrix)
        if size == 1:
            return matrix[0][0]
        elif size == 2:
            return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
        else:
            det = 0
            for col in range(size):
                submatrix = []
                for i in range(1, len(matrix)):
                    subrow = []
                    for j in range(len(matrix[i])):
                        if j != col:
                            subrow.append(matrix[i][j])
                    submatrix.append(subrow)
                cofactor = matrix[0][col] * self.determinant(submatrix)
                if col % 2 == 0:
                    det += cofactor
                else:
                    det -= cofactor
            return det

    def inverse_matrix(self, matrix):
        size = len(matrix)
        det = self.determinant(matrix)
        inverse = [[0] * size for _ in range(size)]

        for i in range(size):
            for j in range(size):
                submatrix = []
                for row_idx in range(len(matrix)):
                    if row_idx != i:
                        subrow = []
                        for col_idx in range(len(matrix[row_idx])):
                            if col_idx != j:
                                subrow.append(matrix[row_idx][col_idx])
                        submatrix.append(subrow)
                cofactor = self.determinant(submatrix)
                try:
                    if (i + j) % 2 == 0:
                        inverse[j][i] = cofactor / det
                    else:
                        inverse[j][i] = -cofactor / det
                except ZeroDivisionError:
                    print("ZERO DIVISION")
                    exit()
        print(inverse)
        return inverse

    def __truediv__(self, other):
        matrix_Division = []
        other_inverse = self.inverse_matrix(other)
        for i in range(len(self.matrix)):
            row = []
            for j in range(len(other_inverse[0])):
                dot_product = 0
                for k in range(len(other_inverse)):
                    dot_product += self.matrix[i][k] * other_inverse[k][j]
                row.append(dot_product)
            matrix_Division.append(row)
        return matrix_Division

    def save_result(self, output_filename, other_matrix):
        matrix_sum = self + other_matrix
        matrix_sub = self - other_matrix
        matrix_mult = self * other_matrix
        matrix_div = self / other_matrix

        with open(output_filename, 'w') as file:
            file.write("Matrix Sum:\n")
            for row in range(len(matrix_sum)):
                file.write(str(matrix_sum[row]) + '\n')

            file.write("Matrix Sub:\n")
            for row in range(len(matrix_sub)):
                file.write(str(matrix_sub[row]) + '\n')

            file.write("Matrix Mult:\n")
            for row in range(len(matrix_mult)):
                file.write(str(matrix_sum[row]) + '\n')

            file.write("Matrix Div:\n")
            for row in range(len(matrix_div)):
                file.write(str(matrix_div[row]) + '\n')


# Your existing code
filename1 = 'FMatrix.txt'
filename2 = 'SMatrix.txt'
output_filename = 'OutputMatrix.txt'

matrix_ops1 = Matrix(filename1)
matrix_ops1.load_matrix()
matrix_ops2 = Matrix(filename2)
matrix_ops2.load_matrix()
matrix_ops1.save_result(output_filename, matrix_ops2.matrix)
