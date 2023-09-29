import sys


class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def from_file(file_path):
        matrix = []
        try:
            with open(file_path, 'r') as file:
                for line in file:
                    row = [int(x) for x in line.strip().split()]
                    matrix.append(row)
        except FileNotFoundError:
            print("Error reading file", file_path)
            sys.exit(0)  # Зупиняємо програму з кодом помилки 1
        return Matrix(matrix)

    def to_file(self, filename):
        try:
            with open(filename, 'w') as f:
                for row in self.matrix:
                    f.write(' '.join(['{:0.5g}'.format(x) for x in row]) + '\n')
        except Exception as e:
            return f"Error writing matrix to '{filename}': {e}"

    def __add__(self, other_matrix):
        if len(self.matrix) != len(other_matrix.matrix) or len(self.matrix[0]) != len(other_matrix.matrix[0]):
            raise ValueError("Matrix dimensions do not match")

        result = []
        for i in range(len(self.matrix)):
            row = []
            for j in range(len(self.matrix[0])):
                row.append(self.matrix[i][j] + other_matrix.matrix[i][j])
            result.append(row)
        return Matrix(result)

    def __sub__(self, other_matrix):
        if len(self.matrix) != len(other_matrix.matrix) or len(self.matrix[0]) != len(other_matrix.matrix[0]):
            raise ValueError("Matrix dimensions do not match")

        result = []
        for i in range(len(self.matrix)):
            row = []
            for j in range(len(self.matrix[0])):
                row.append(self.matrix[i][j] - other_matrix.matrix[i][j])
            result.append(row)
        return Matrix(result)

    def __mul__(self, other_matrix):
        if len(self.matrix[0]) != len(other_matrix.matrix):
            raise ValueError("Invalid matrix dimensions for multiplication")

        result = []
        for i in range(len(self.matrix)):
            row = []
            for j in range(len(other_matrix.matrix[0])):
                sum_product = 0
                for k in range(len(other_matrix.matrix)):
                    sum_product += self.matrix[i][k] * other_matrix.matrix[k][j]
                row.append(sum_product)
            result.append(row)
        return Matrix(result)

    def det2(self):
        return self.matrix[0][0] * self.matrix[1][1] - self.matrix[0][1] * self.matrix[1][0]

    def inv2(self):
        d = self.det2()
        return Matrix(
            [[self.matrix[1][1] / d, -self.matrix[0][1] / d], [-self.matrix[1][0] / d, self.matrix[0][0] / d]])

    def det3(self):
        ret = 0
        for i in range(3):
            pos = 1
            neg = 1
            for j in range(3):
                pos *= self.matrix[j][(i + j) % 3]
                neg *= self.matrix[j][(i - j) % 3]
            ret += (pos - neg)
        return ret

    def inv3(self):
        ret = [3 * [0] for _ in range(3)]
        det = self.det3()
        for i in range(3):
            for j in range(3):
                adj = [[n for ii, n in enumerate(row) if ii != i]
                       for jj, row in enumerate(self.matrix) if jj != j]
                d = adj[0][0] * adj[1][1] - adj[0][1] * adj[1][0]
                sgn = (-1) ** (i + j)
                ret[i][j] = sgn * d / det
        return Matrix(ret)

    def __truediv__(self, other_matrix):
        result = None
        try:
            if len(other_matrix.matrix) != len(other_matrix.matrix[0]):
                raise ValueError("matrix_b must be a square matrix for inversion")

            if len(self.matrix[0]) != len(other_matrix.matrix):
                raise ValueError("Invalid matrix dimensions for division")

            if len(other_matrix.matrix) == 2:
                det = other_matrix.det2()
                if det == 0:
                    raise ValueError("matrix_b is singular; cannot be inverted")
                inv = other_matrix.inv2()
            elif len(other_matrix.matrix) == 3:
                det = other_matrix.det3()
                if det == 0:
                    raise ValueError("matrix_b is singular; cannot be inverted")
                inv = other_matrix.inv3()
            else:
                raise ValueError("Unsupported matrix dimensions")

            result = self.__mul__(inv)
        except Exception as e:
            print(f"Error performing division: {e}")
        return result

result = None
MatrixA = Matrix.from_file('../Task(Matrix and vectors)/matrix_A.txt')
MatrixB = Matrix.from_file('../Task(Matrix and vectors)/matrix_B.txt')
try:
    operation = input("Enter operation (add, subtract, multiply, divide): ")
    if operation == 'add':
        result = MatrixA + MatrixB
    elif operation == 'subtract':
        result = MatrixA - MatrixB
    elif operation == 'multiply':
        result = MatrixA * MatrixB
    elif operation == 'divide':
        result = MatrixA / MatrixB
    else:
        raise ValueError("Invalid operation")

except ValueError as e:
    print(f"Error performing operation: {e}")

try:
    if result is not None:
        for row in result.matrix:
            print(' '.join(['{:0.5g}'.format(x) for x in row]))
except TypeError:
    pass

try:
    if result is not None:
        result.to_file('result_matrix.txt')
except Exception as e:
    print(f"Error writing matrix to file: {e}")
