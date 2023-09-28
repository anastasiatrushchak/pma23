import Constants

class Matrix:
    def __init__(self, file_path1, file_path2):
        self.matrix1 = self.read_matrix_from_file(file_path1)
        self.matrix2 = self.read_matrix_from_file(file_path2)

    @staticmethod
    def read_matrix_from_file(file_path):
        matrix = []
        try:
            with open(file_path, 'r') as readFile:
                for line in readFile:
                    line = line.strip()
                    row = [int(i) for i in line.split(Constants.SEPARATOR)]
                    matrix.append(row)
            return matrix
        except FileNotFoundError as e:
            print("Error: File not found",e)
            return None
        except Exception as e:
            print("An unexpected error occurred",e)
            return None

    def __add__(self, other):
        if len(self.matrix1) != len(other.matrix2) or len(self.matrix1[0]) != len(other.matrix2[0]):
            print("Error: Matrices must have the same dimensions for addition")
            return None

        addition = []
        for i in range(len(self.matrix1)):
            row = []
            for j in range(len(self.matrix1[0])):
                row.append(self.matrix1[i][j] + other.matrix2[i][j])
            addition.append(row)
        return addition

    def __sub__(self, other):
        if len(self.matrix1) != len(other.matrix2) or len(self.matrix1[0]) != len(other.matrix2[0]):
            print("Error: Matrices must have the same dimensions for subtraction")
            return None

        subtraction = []
        for i in range(len(self.matrix1)):
            row = []
            for j in range(len(self.matrix1[0])):
                row.append(self.matrix1[i][j] - other.matrix2[i][j])
            subtraction.append(row)
        return subtraction

    def __mul__(self, other):
        if len(self.matrix1[0]) != len(other.matrix2):
            print("Error: Number of columns in the first matrix must be equal to the number of rows in the second matrix")
            return None

        multiplication = []
        for i in range(len(self.matrix1)):
            row = []
            for j in range(len(other.matrix2[0])):
                product = 0
                for k in range(len(other.matrix2)):
                    product += self.matrix1[i][k] * other.matrix2[k][j]
                row.append(product)
            multiplication.append(row)
        return multiplication

    def __truediv__(self, other):
        try:
            det = self.determinant(other.matrix2)

            if det == 0:
                raise ValueError("The determinant of the second matrix is zero, division is not possible")

            transposed = []
            for i in range(len(self.matrix1)):
                transposed.append([])
                for j in range(len(self.matrix1[0])):
                    transposed[i].append(self.cofactor(other.matrix2, i, j))
            transposed = self.transpose(transposed)

            inverse = []
            for i in range(len(transposed)):
                inverse.append([])
                for j in range(len(transposed[0])):
                    value = float(transposed[i][j]) / det
                    inverse[i].append(round(value, 2))

            result = self.multiplication_for_divide(self.matrix1, inverse)

            for i in range(len(result)):
                for j in range(len(result[0])):
                    result[i][j] = round(result[i][j], 2)
            return result
        except ZeroDivisionError as e:
            print("Error: Different sizes are specified in the file", e)

    @staticmethod
    def determinant(matrix):
        det = 0
        for i in range(len(matrix)):
            add = 1
            sub = 1
            for j in range(len(matrix)):
                add *= matrix[j][(i + j) % len(matrix)]
                sub *= matrix[j][(i - j) % len(matrix)]
            det += (add - sub)
        if det == 0:
            raise ValueError("The determinant cannot be equal to 0")
        return det

    @staticmethod
    def transpose(matrix):
        rows = len(matrix)
        cols = len(matrix[0])
        result = [[None] * rows for _ in range(cols)]
        for i in range(rows):
            for j in range(cols):
                result[j][i] = matrix[i][j]
        return result

    def cofactor(self, matrix, row, col):
        addition = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i != row and j != col:
                    addition.append(matrix[i][j])
        result = ((-1) ** (row + col)) * (addition[0] * addition[3] - addition[2] * addition[1])
        return result

    def multiplication_for_divide(self, matrix1, matrix2):
        multiplication = []
        for i in range(len(matrix1)):
            row = []
            for j in range(len(matrix2[0])):
                product = 0
                for k in range(len(matrix2)):
                    product += matrix1[i][k] * matrix2[k][j]
                row.append(product)
            multiplication.append(row)
        return multiplication


class Vector:
    def __init__(self, file_path1, file_path2):
        self.vector1 = self.read_vector_from_file(file_path1)
        self.vector2 = self.read_vector_from_file(file_path2)
    @staticmethod
    def read_vector_from_file(file_path):
        vector = []
        try:
            with open(file_path, 'r') as readFile:
                for line in readFile:
                    line = line.strip()
                    row = [int(i) for i in line.split(Constants.SEPARATOR)]
                    vector.append(row)
            return vector
        except FileNotFoundError as e:
            print(f"Error: File not found - {e}")
            return None
        except Exception as e:
            print(f"An unexpected error occurred - {e}")
            return None

    def __add__(self, other):
        if len(self.vector1) != len(other.vector2):
            print("Error: Vectors must have the same length for addition")
            return None

        add_vector = []
        for i in range(len(self.vector1)):
            result_row = []
            for j in range(len(self.vector1[i])):
                result_row.append(self.vector1[i][j] + other.vector2[i][j])
            add_vector.append(result_row)
        return add_vector

    def __sub__(self, other):
        if len(self.vector1) != len(other.vector2):
            print("Error: Vectors must have the same length for subtraction")
            return None

        sub_vector = []
        for i in range(len(self.vector1)):
            result_row = []
            for j in range(len(self.vector1[i])):
                result_row.append(self.vector1[i][j] - other.vector2[i][j])
            sub_vector.append(result_row)
        return sub_vector

    def __mul__(self, other):
        if len(self.vector1) != len(other.vector2):
            print("Error: Vectors must have the same length for element-wise multiplication")
            return None

        mul_vector = []
        for i in range(len(self.vector1)):
            result_row = []
            for j in range(len(self.vector1[i])):
                result_row.append(self.vector1[i][j] * other.vector2[i][j])
            mul_vector.append(result_row)
        return mul_vector

    def __truediv__(self, other):
        try:
            if len(self.vector1) != len(other.vector2):
                print("Error: Vectors must have the same length for element-wise division")
                return None

            div_vector = []
            for i in range(len(self.vector1)):
                result_row = []
                for j in range(len(self.vector1[i])):
                    if other.vector2[i][j] == 0:
                        print("Error: Division by zero is not allowed")
                        return None
                    result_row.append(self.vector1[i][j] / other.vector2[i][j])
                div_vector.append(result_row)
            return div_vector
        except ZeroDivisionError as e:
            print("Error: Division by zero is not allowed", e)


try:
    matrix = Matrix(Constants.Input_Matrix_1, Constants.Input_Matrix_2)
    vector = Vector(Constants.Input_Vector_1, Constants.Input_Vector_2)

    with open("output2.txt", "w") as file:
        choice = input("Matrix or Vector? (M or V): ")
        operation = input("Enter the operation (+, -, *, /): ")

        if choice == "M":
            if operation == "+":
                result = matrix + matrix
            elif operation == "-":
                result = matrix - matrix
            elif operation == "*":
                result = matrix * matrix
            elif operation == "/":
                result = matrix / matrix
            else:
                print("Error: There is no such operator for matrices")

            if result:
                for row in result:
                    file.write(' '.join(map(str, row)) + '\n')

        elif choice == "V":
            if operation == "+":
                result = vector + vector
            elif operation == "-":
                result = vector - vector
            elif operation == "*":
                result = vector * vector
            elif operation == "/":
                result = vector / vector
            else:
                print("Error: There is no such operator for vectors")

            if result:
                for item in result:
                    file.write(str(item) + '\n')
        else:
            print("Error: Invalid choice.")
except ValueError as e:
    print("Error: Different sizes are specified in the file", e)
except EOFError as e:
    print("Error: Empty file", e)
except FileNotFoundError as e:
    print("Error: One or more files not found.", e)
except (IOError) as e:
    print("Error: Incorrect input/output during file operations", e)
except Exception as e:
    print("An unexpected error occurred", e)
