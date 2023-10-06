class Matrix:
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.data = [[0 for _ in range(columns)] for _ in range(rows)]

    def set_element(self, i, j, value):
        self.data[i][j] = value

    def get_element(self, i, j):
        return self.data[i][j]

    def add(self, other):
        if self.rows != other.rows or self.columns != other.columns:
            raise ValueError("Matrices must have the same dimensions for addition")
        result = Matrix(self.rows, self.columns)
        for i in range(self.rows):
            for j in range(self.columns):
                result.set_element(i, j, self.get_element(i, j) + other.get_element(i, j))
        return result

    def subtract(self, other):
        if self.rows != other.rows or self.columns != other.columns:
            raise ValueError("Matrices must have the same dimensions for subtraction")
        result = Matrix(self.rows, self.columns)
        for i in range(self.rows):
            for j in range(self.columns):
                result.set_element(i, j, self.get_element(i, j) - other.get_element(i, j))
        return result

    def multiply(self, other):
        if self.columns != other.rows:
            raise ValueError("Number of columns in the first matrix must be equal to the number of rows in the second matrix")
        result = Matrix(self.rows, other.columns)
        for i in range(self.rows):
            for j in range(other.columns):
                total = 0
                for k in range(self.columns):
                    total += self.get_element(i, k) * other.get_element(k, j)
                result.set_element(i, j, total)
        return result

    def divide(self, scalar):
        result = Matrix(self.rows, self.columns)
        for i in range(self.rows):
            for j in range(self.columns):
                result.set_element(i, j, self.get_element(i, j) / scalar)
        return result

    def display(self):
        for i in range(self.rows):
            for j in range(self.columns):
                print(self.get_element(i, j), end=" ")
            print()

    @classmethod
    def from_file(cls, filename):
        with open(filename, 'r') as file:
            lines = file.readlines()
            rows = len(lines)
            columns = len(lines[0].split())
            matrix = cls(rows, columns)
            for i, line in enumerate(lines):
                values = line.split()
                for j, value in enumerate(values):
                    matrix.set_element(i, j, int(value))
            return matrix

    def to_file(self, filename):
        with open(filename, 'w') as file:
            for row in self.data:
                file.write(' '.join(map(str, row)) + '\n')


if __name__ == "__main__":
    # Зчитування матриць з файлів
    matrix1 = Matrix.from_file('matrix1.txt')
    matrix2 = Matrix.from_file('matrix2.txt')

    # Відкриття файлу для запису результатів
    with open('results.txt', 'w') as results_file:
        # Додавання
        result_addition = matrix1.add(matrix2)
        results_file.write(f"Addition:\n")
        result_addition.to_file('result_addition.txt')

        # Віднімання
        result_subtraction = matrix1.subtract(matrix2)
        results_file.write(f"\nSubtraction:\n")
        result_subtraction.to_file('result_subtraction.txt')

        # Множення
        result_multiplication = matrix1.multiply(matrix2)
        results_file.write(f"\nMultiplication:\n")
        result_multiplication.to_file('result_multiplication.txt')

        # Ділення
        scalar = 2
        result_division = matrix1.divide(scalar)
        results_file.write(f"\nDivision by {scalar}:\n")
        result_division.to_file('result_division.txt')
