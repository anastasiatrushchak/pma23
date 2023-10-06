class Vector:
    def __init__(self, values):
        self.values = values

    def __add__(self, other):
        if len(self.values) != len(other.values):
            raise ValueError("Vectors must have the same length for addition")
        result = [x + y for x, y in zip(self.values, other.values)]
        return Vector(result)

    def __sub__(self, other):
        if len(self.values) != len(other.values):
            raise ValueError("Vectors must have the same length for subtraction")
        result = [x - y for x, y in zip(self.values, other.values)]
        return Vector(result)

    def __mul__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            result = [x * other for x in self.values]
            return Vector(result)
        elif isinstance(other, Vector):
            if len(self.values) != len(other.values):
                raise ValueError("Vectors must have the same length for element-wise multiplication")
            result = [x * y for x, y in zip(self.values, other.values)]
            return Vector(result)
        else:
            raise TypeError("Unsupported operand type")

    def __truediv__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            result = [x / other for x in self.values]
            return Vector(result)
        else:
            raise TypeError("Unsupported operand type")

    def __str__(self):
        return str(self.values)

    @classmethod
    def from_file(cls, filename):
        with open(filename, 'r') as file:
            values = [int(num) for num in file.read().split()]
        return cls(values)

    def to_file(self, filename):
        with open(filename, 'w') as file:
            file.write(' '.join(map(str, self.values)))

if __name__ == "__main__":
    v1 = Vector.from_file('vector1.txt')
    v2 = Vector.from_file('vector2.txt')

    with open('results.txt', 'w') as results_file:
        result_addition = v1 + v2
        results_file.write(f"Addition: {result_addition}\n")
        result_addition.to_file('result_addition.txt')

        result_subtraction = v1 - v2
        results_file.write(f"Subtraction: {result_subtraction}\n")
        result_subtraction.to_file('result_subtraction.txt')

        result_scalar_multiplication = v1 * 2
        results_file.write(f"Scalar Multiplication: {result_scalar_multiplication}\n")
        result_scalar_multiplication.to_file('result_scalar_multiplication.txt')

        result_elementwise_multiplication = v1 * v2
        results_file.write(f"Elementwise Multiplication: {result_elementwise_multiplication}\n")
        result_elementwise_multiplication.to_file('result_elementwise_multiplication.txt')

        result_scalar_division = v1 / 2
        results_file.write(f"Scalar Division: {result_scalar_division}\n")
        result_scalar_division.to_file('result_scalar_division.txt')
