class MatrixApp:
    def __init__(self, matrix_a, matrix_b):
        self.matrix_a = matrix_a
        self.matrix_b = matrix_b

    @staticmethod
    def read_matrix(filename):
        try:
            with open(filename, "r") as file:
                lines = file.readlines()
                matrix_a = [list(map(int, lines[i].strip().split())) for i in range(2)]
                matrix_b = [list(map(int, lines[i].strip().split())) for i in range(3, 5)]
                return matrix_a, matrix_b
        except FileNotFoundError:
            print("File not found")

    @staticmethod
    def write_matrix(filename, operation, result):
        with open(filename, "a") as file:
            file.write(f"{operation}:\n")
            for row in result:
                file.write(" ".join(map(str, row)) + "\n")

    @staticmethod
    def multiply_matrices(matrix_a, matrix_b):
        result = [[0, 0], [0, 0]]
        for i in range(2):
            for j in range(2):
                for k in range(2):
                    result[i][j] += matrix_a[i][k] * matrix_b[k][j]
        return result

    @staticmethod
    def add_matrices(matrix_a, matrix_b):
        result = [[0, 0], [0, 0]]
        for i in range(2):
            for j in range(2):
                result[i][j] = matrix_a[i][j] + matrix_b[i][j]
        return result

    @staticmethod
    def subtract_matrices(matrix_a, matrix_b):
        result = [[0, 0], [0, 0]]
        for i in range(2):
            for j in range(2):
                result[i][j] = matrix_a[i][j] - matrix_b[i][j]
        return result

    @staticmethod
    def inverse_matrix(matrix):
        det = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
        if det == 0:
            raise ValueError("Determinant is 0.")

        inverse_det = 1.0 / det
        result = [[0, 0], [0, 0]]

        for i in range(2):
            for j in range(2):
                result[i][j] = matrix[1 - i][1 - j] * inverse_det
        return result

    @staticmethod
    def divide_matrices(matrix_a, matrix_b):
        try:
            inverse_b = MatrixApp.inverse_matrix(matrix_b)
        except ValueError as e:
            print(f"Error: {str(e)}")
            inverse_b = None

        if inverse_b:
            result = MatrixApp.multiply_matrices(matrix_a, inverse_b)
            return result
        else:
            return None

    def process_matrix(self, output_file):
        result_addition = self.add_matrices(self.matrix_a, self.matrix_b)
        result_subtraction = self.subtract_matrices(self.matrix_a, self.matrix_b)
        result_multiplication = self.multiply_matrices(self.matrix_a, self.matrix_b)
        result_division = self.divide_matrices(self.matrix_a, self.matrix_b)

        with open(output_file, 'w') as file:
            if result_division is not None:
                self.write_matrix(output_file, "Addition", result_addition)
                self.write_matrix(output_file, "Subtraction", result_subtraction)
                self.write_matrix(output_file, "Multiplication", result_multiplication)
                self.write_matrix(output_file, "Division", result_division)


def main():
    input_file = 'input.txt'
    output_file = 'output.txt'

    matrix_a, matrix_b = MatrixApp.read_matrix(input_file)
    app = MatrixApp(matrix_a, matrix_b)
    app.process_matrix(output_file)

if __name__ == "__main__":
    main()

