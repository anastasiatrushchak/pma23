import numpy as np  # Потрібно встановити бібліотеку NumPy

INPUT_CODE = "input.txt"
OUTPUT_CODE = "output.txt"
with open(INPUT_CODE, "r") as read_code:
    array_fibonacci = read_code.read().split("\n")

array_fibonacci = [float(i) for i in array_fibonacci if i.isdigit()]
for i in range(2, 10):
    array_fibonacci.append((array_fibonacci[i - 2]) + array_fibonacci[i - 1])

with open(OUTPUT_CODE, "w") as output_file:
    output_file.write(str(array_fibonacci))


def add_matrices(matrix1, matrix2):
    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix1[0])):
            row.append(matrix1[i][j] + matrix2[i][j])
        result.append(row)
    return result


def subtract_matrices(matrix1, matrix2):
    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix1[0])):
            row.append(matrix1[i][j] - matrix2[i][j])
        result.append(row)
    return result


def multiply_matrices(matrix1, matrix2):
    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix2[0])):
            sum = 0
            for k in range(len(matrix2)):
                sum += matrix1[i][k] * matrix2[k][j]
            row.append(sum)
        result.append(row)
    return result


def inverse_matrix(matrix):
    try:
        inverse = np.linalg.inv(matrix)
        return inverse.tolist()
    except np.linalg.LinAlgError:
        return "Матриця не має оберненої матриці (детермінант дорівнює нулю)."


def add_vectors(vector1, vector2):
    if len(vector1) != len(vector2):
        raise ValueError("Вектори мають бути однакової довжини.")
    result = [x + y for x, y in zip(vector1, vector2)]
    return result


def subtract_vectors(vector1, vector2):
    if len(vector1) != len(vector2):
        raise ValueError("Вектори мають бути однакової довжини.")
    result = [x - y for x, y in zip(vector1, vector2)]
    return result


def multiply_vectors(vector1, vector2):
    if len(vector1) != len(vector2):
        raise ValueError("Вектори мають бути однакової довжини.")
    result = [x * y for x, y in zip(vector1, vector2)]
    return result


def divide_vectors(vector1, vector2):
    if len(vector1) != len(vector2):
        raise ValueError("Вектори мають бути однакової довжини.")
    result = [x / y for x, y in zip(vector1, vector2)]
    return result


class Matrix:
    def __init__(self, data):
        self.data = data

    def __str__(self):
        return "\n".join([" ".join(map(str, row)) for row in self.data])

    def __add__(self, other):
        if len(self.data) != len(other.data) or len(self.data[0]) != len(other.data[0]):
            raise ValueError("Розміри матриць не співпадають")
        result_data = [[self.data[i][j] + other.data[i][j] for j in range(len(self.data[0]))] for i in
                       range(len(self.data))]
        return Matrix(result_data)

    def __sub__(self, other):
        if len(self.data) != len(other.data) or len(self.data[0]) != len(other.data[0]):
            raise ValueError("Розміри матриць не співпадають")
        result_data = [[self.data[i][j] - other.data[i][j] for j in range(len(self.data[0]))] for i in
                       range(len(self.data))]
        return Matrix(result_data)

    def __mul__(self, other):
        if len(self.data[0]) != len(other.data):
            raise ValueError("Кількість стовпців першої матриці не дорівнює кількості рядків другої матриці")
        result_data = [[sum(self.data[i][k] * other.data[k][j] for k in range(len(self.data[0]))) for j in
                        range(len(other.data[0]))] for i in range(len(self.data))]
        return Matrix(result_data)

    def __truediv__(self, other):
        if len(self.data) != len(other.data) or len(self.data[0]) != len(other.data[0]):
            raise ValueError("Розміри матриць не співпадають")
        result_data = [[self.data[i][j] / other.data[i][j] for j in range(len(self.data[0]))] for i in
                       range(len(self.data))]
        return Matrix(result_data)


matrix1 = Matrix([[1, 2], [3, 4]])
matrix2 = Matrix([[5, 6], [7, 8]])

result_add = matrix1 + matrix2
result_sub = matrix1 - matrix2
result_mul = matrix1 * matrix2
result_div = matrix1 / matrix2

print("Матриця1:")
print(matrix1)
print("Матриця2:")
print(matrix2)
print("Результат додавання:")
print(result_add)
print("Результат віднімання:")
print(result_sub)
print("Результат множення:")
print(result_mul)
print("Результат ділення:")
print(result_div)


class Vector:
    def __init__(self, data):
        self.data = data

    def __str__(self):
        return " ".join(map(str, self.data))

    def __add__(self, other):
        if len(self.data) != len(other.data):
            raise ValueError("Довжина векторів не співпадає")
        result_data = [x + y for x, y in zip(self.data, other.data)]
        return Vector(result_data)

    def __sub__(self, other):
        if len(self.data) != len(other.data):
            raise ValueError("Довжина векторів не співпадає")
        result_data = [x - y for x, y in zip(self.data, other.data)]
        return Vector(result_data)

    def __mul__(self, scalar):
        result_data = [x * scalar for x in self.data]
        return Vector(result_data)

    def __truediv__(self, scalar):
        if scalar == 0:
            raise ValueError("Ділення на нуль неможливе")
        result_data = [x / scalar for x in self.data]
        return Vector(result_data)


vector1 = Vector([1, 2, 3])
vector2 = Vector([4, 5, 6])

result_add = vector1 + vector2
result_sub = vector1 - vector2
result_mul = vector1 * 2
result_div = vector1 / 2

print("Вектор1:")
print(vector1)
print("Вектор2:")
print(vector2)
print("Результат додавання:")
print(result_add)
print("Результат віднімання:")
print(result_sub)
print("Результат множення:")
print(result_mul)
print("Результат ділення:")
print(result_div)


