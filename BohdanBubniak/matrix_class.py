class Matrix:
    def __init__(self, data):
        self.data = data
        self.rows = len(data)
        self.cols = len(data[0])

    @staticmethod
    def read_from_file(filename):
        with open(filename, 'r') as file:
            data = [list(map(int, line.strip().split())) for line in file]
        return Matrix(data)

    @staticmethod
    def write_to_file(filename, matrix):
        with open(filename, 'a') as file:
            for row in matrix.data:
                file.write(' '.join(map(str, row)) + '\n')
            file.write('\n')

    def __add__(self, other):
        result = []
        for i in range(self.rows):
            row = []
            for j in range(self.cols):
                row.append(self.data[i][j] + other.data[i][j])
            result.append(row)
        return Matrix(result)

    def __sub__(self, other):
        result = []
        for i in range(self.rows):
            row = []
            for j in range(self.cols):
                row.append(self.data[i][j] - other.data[i][j])
            result.append(row)
        return Matrix(result)

    def __mul__(self, other):
        result = []
        for i in range(self.rows):
            row = []
            for j in range(other.cols):
                cell_value = sum(self.data[i][k] * other.data[k][j] for k in range(self.cols))
                row.append(cell_value)
            result.append(row)
        return Matrix(result)

    def inverse(self):
        det = self.data[0][0] * self.data[1][1] - self.data[0][1] * self.data[1][0]
        return Matrix([[self.data[1][1]/det, -self.data[0][1]/det], 
                       [-self.data[1][0]/det, self.data[0][0]/det]])

    def __truediv__(self, other):
        inv_other = other.inverse()
        return self * inv_other

    def __str__(self):
        return '\n'.join([' '.join(map(str, row)) for row in self.data])

matrixA = Matrix.read_from_file('matrixA.txt')
matrixB = Matrix.read_from_file('matrixB.txt')

result_add = matrixA + matrixB
result_subtract = matrixA - matrixB
result_multiply = matrixA * matrixB
result_divide = matrixA / matrixB

Matrix.write_to_file('result.txt', result_add)
Matrix.write_to_file('result.txt', result_subtract)
Matrix.write_to_file('result.txt', result_multiply)
Matrix.write_to_file('result.txt', result_divide)
