class MatrixApp:
    def __init__(self, input_file, output_file):
        self.input_file = input_file
        self.output_file = output_file

    @staticmethod
    def read_matrix(filename):
         try:
            with open(filename, "r") as file:
                lines = file.readlines()
                matrix_a = []
                matrix_b = []
                for i in range(2):
                    row = [int(x) for x in lines[i].strip().split()]
                    matrix_a.append(row)

                for i in range(3, 5):
                    row = [int(x) for x in lines[i].strip().split()]
                    matrix_b.append(row)
                return matrix_a, matrix_b
        except FileNotFoundError:
            print("file not found")

    @staticmethod
    def write_matrix(filename, result_addition, result_subtraction, result_multiplication, result_division):
        with open(filename, "a") as file:
            file.write("addition:\n")
            for row in result_addition:
                file.write(" ".join(map(str, row)) + "\n")

            file.write("\nsubtraction:\n")
            for row in result_subtraction:
                file.write(" ".join(map(str, row)) + "\n")

            file.write("\nmultiplication:\n")
            for row in result_multiplication:
                file.write(" ".join(map(str, row)) + "\n")

            file.write("\ndivision:\n")
            for row in result_division:
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
        result[0][0] = matrix[1][1] * inverse_det
        result[0][1] = -matrix[0][1] * inverse_det
        result[1][0] = -matrix[1][0] * inverse_det
        result[1][1] = matrix[0][0] * inverse_det
        return result

    @staticmethod
    def divide_matrices(matrix_a, matrix_b):
        inverse_b = MatrixApp.inverse_matrix(matrix_b)
        result = MatrixApp.multiply_matrices(matrix_a, inverse_b)
        return result

    def process_matrix(self):
        matrix_a, matrix_b = self.read_matrix(self.input_file)
        result_addition = self.add_matrices(matrix_a, matrix_b)
        result_subtraction = self.subtract_matrices(matrix_a, matrix_b)
        result_multiplication = self.multiply_matrices(matrix_a, matrix_b)
        result_division = self.divide_matrices(matrix_a, matrix_b)

        with open(self.output_file, 'w') as file:
            self.write_matrix(self.output_file, result_addition, result_subtraction, result_multiplication, result_division)


def main():
    input_file = 'input.txt'
    output_file = 'output.txt'

    calculator = MatrixApp(input_file, output_file)
    calculator.process_matrix()


if __name__ == "__main__":
    main()
