class Matrix:
    def __init__(self, rows, columns, data=None):
        self.rows = rows
        self.columns = columns
        if data is not None:
            self.data = data
        else:
            self.data = [[0] * columns for _ in range(rows)]

    def set_value(self, row, col, value):
        if 0 <= row < self.rows and 0 <= col < self.columns:
            self.data[row][col] = value
        else:
            print("Invalid row or column index")

    def get_value(self, row, col):
        if 0 <= row < self.rows and 0 <= col < self.columns:
            return self.data[row][col]
        else:
            print("Invalid row or column index")

    def __sub__(self, other):
        if self.rows != other.rows or self.columns != other.columns:
            print("Matrix dimensions do not match for subtraction.")
            return None

        result_minus = []
        for i in range(self.rows):
            result_minus.append([self.data[i][j] - other.data[i][j] for j in range(self.columns)])

        return Matrix(self.rows, self.columns, result_minus)

    def __add__(self, other):
        if self.rows != other.rows or self.columns != other.columns:
            print("Matrix dimensions do not match for addition.")
            return None
        result_plus = []
        for i in range(self.rows):
            result_plus.append([self.data[i][j] + other.data[i][j] for j in range(self.columns)])

        return Matrix(self.rows, self.columns, result_plus)

    def multiply(self, other):
        if self.columns != other.rows:
            print(
                "Number of columns in the first matrix must be equal to the number of rows in the second matrix for multiplication.")
            return None

        result_multiply = []
        for i in range(self.rows):
            row = []
            for j in range(other.columns):
                product = 0
                for k in range(self.columns):
                    product += self.data[i][k] * other.data[k][j]
                row.append(product)
            result_multiply.append(row)

        return Matrix(self.rows, other.columns, result_multiply)

    def inverse(self):
        if self.rows != self.columns:
            print("Matrix is not square, cannot be inverted.")
            return None
        augmented_matrix = []
        for i in range(self.rows):
            row = self.data[i] + [0] * self.rows
            row[i + self.rows] = 1
            augmented_matrix.append(row)
        for i in range(self.rows):
            pivot = augmented_matrix[i][i]
            if pivot == 0:
                print("Matrix is singular and cannot be inverted.")
                return None
            for j in range(self.rows * 2):
                augmented_matrix[i][j] /= pivot

            for k in range(self.rows):
                if k != i:
                    factor = augmented_matrix[k][i]
                    for j in range(self.rows * 2):
                        augmented_matrix[k][j] -= factor * augmented_matrix[i][j]
            inverted_matrix_data = [row[self.rows:] for row in augmented_matrix]

            return Matrix(self.rows, self.columns, inverted_matrix_data)

    def divide(self, other):
        if self.rows != other.rows or self.columns != other.columns:
            print("Matrix dimensions do not match for division.")
            return None

        inverse_other = other.inverse()
        if not inverse_other:
            return None


        result_multiply = self.multiply(inverse_other)
        if not result_multiply:
            print("Division result is not defined.")
            return None

        return result_multiply


    def __str__(self):
        return "\n".join(["\t".join(map(str, row)) for row in self.data])

    def save_to_file(self, filename):
        try:
            with open(filename, 'w') as file:
                for row in self.data:
                    file.write("\t".join(map(str, row)) + "\n")
        except Exception as e:
            print(f"Error while saving to file '{filename}': {str(e)}")


def read_matrix_from_file(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            rows = len(lines)
            columns = len(lines[0].strip().split())
            matrix_data = []

            for line in lines:
                values = list(map(int, line.strip().split()))
                matrix_data.append(values)

            return Matrix(rows, columns, matrix_data)
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
        return None


first_matrix = read_matrix_from_file("arr_first.txt")
second_matrix = read_matrix_from_file("arr_second.txt")

if first_matrix and second_matrix:
    with open("Result.txt", 'w') as result_file:

        result_file.write("First Matrix:\n")
        result_file.write(str(first_matrix))
        result_file.write("\n\nSecond Matrix:\n")
        result_file.write(str(second_matrix))
        result_file.write("\n\n")

        result_addition = first_matrix + second_matrix
        result_subtraction = first_matrix - second_matrix
        result_multiplication = first_matrix.multiply(second_matrix)
        result_division = first_matrix.divide(second_matrix)

        if result_addition:
            result_file.write("Sum:\n")
            result_file.write(str(result_addition))
            result_file.write("\n\n")

        if result_subtraction:
            result_file.write("Difference :\n")
            result_file.write(str(result_subtraction))
            result_file.write("\n\n")

        if result_multiplication:
            result_file.write("Multiplication:\n")
            result_file.write(str(result_multiplication))
            result_file.write("\n\n")

        if result_division:
            result_file.write("Division of the First Matrix by the Second Matrix:\n")
            result_file.write(str(result_division))
            result_file.write("\n\n")
