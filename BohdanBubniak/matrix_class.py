class Matrix:
    def __init__(self, data):
        self.data = data
        self.rows = len(data)
        self.cols = len(data[0])

    @staticmethod
    def read_from_file(filename):
        try:
            with open(filename, 'r') as file:
                data = [list(map(int, line.strip().split())) for line in file]
            return Matrix(data)
        except FileNotFoundError:
            print(f"Error: File {filename} not found.")
        except ValueError:
            print(f"Error: Invalid data format in {filename}.")

    @staticmethod
    def write_to_file(filename, matrix):
        try:
            with open(filename, 'a') as file:
                for row in matrix.data:
                    file.write(' '.join(map(str, row)) + '\n')
                file.write('\n')
        except Exception as e:
            print(f"Error writing to file {filename}: {e}")

    def __add__(self, other):
        result = []
        try:
            for i in range(self.rows):
                row = []
                for j in range(self.cols):
                    row.append(self.data[i][j] + other.data[i][j])
                result.append(row)
            return Matrix(result)
        except IndexError:
            print("Error: Matrices are not of the same size.")

    def __sub__(self, other):
        result = []
        try:
            for i in range(self.rows):
                row = []
                for j in range(self.cols):
                    row.append(self.data[i][j] - other.data[i][j])
                result.append(row)
            return Matrix(result)
        except IndexError:
            print("Error: Matrices are not of the same size.")

    def __mul__(self, other):
        result = []
        try:
            for i in range(self.rows):
                row = []
                for j in range(other.cols):
                    cell_value = sum(self.data[i][k] * other.data[k][j] for k in range(self.cols))
                    row.append(cell_value)
                result.append(row)
            return Matrix(result)
        except IndexError:
            print("Error: Matrix dimensions are incompatible for multiplication.")

    def inverse(self):
        try:
            det = self.data[0][0] * self.data[1][1] - self.data[0][1] * self.data[1][0]
            if det == 0:
                print("Error: Matrix is singular and cannot be inverted.")
                return
            return Matrix([[self.data[1][1]/det, -self.data[0][1]/det], 
                           [-self.data[1][0]/det, self.data[0][0]/det]])
        except IndexError:
            print("Error: Matrix inversion is defined only for 2x2 in this implementation.")

    def __truediv__(self, other):
        try:
            inv_other = other.inverse()
            return self * inv_other
        except Exception as e:
            print(f"Error during division: {e}")

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
