class VectorCalculator:
    def __init__(self, file1, file2):
        self.vector1 = self.read_vector(file1)
        self.vector2 = self.read_vector(file2)
        self.results = {}

    def read_vector(self, filename):
        with open(filename, 'r') as file:
            return [float(line.strip()) for line in file]

    def add(self):
        if len(self.vector1) == len(self.vector2):
            self.results['Додавання'] = [a + b for a, b in zip(self.vector1, self.vector2)]
        else:
            raise ValueError("Вектори мають бути однакової довжини для додавання")

    def subtract(self):
        if len(self.vector1) == len(self.vector2):
            self.results['Віднімання'] = [a - b for a, b in zip(self.vector1, self.vector2)]
        else:
            raise ValueError("Вектори мають бути однакової довжини для віднімання")

    def multiply(self):
        if len(self.vector1) == len(self.vector2):
            self.results['Множення'] = [a * b for a, b in zip(self.vector1, self.vector2)]
        else:
            raise ValueError("Вектори мають бути однакової довжини для множення")

    def divide(self):
        if len(self.vector1) == len(self.vector2):
            self.results['Ділення'] = [a / b for a, b in zip(self.vector1, self.vector2)]
        else:
            raise ValueError("Вектори мають бути однакової довжини для ділення")

    def write_results(self):
        with open('results.txt', 'w') as file:
            for operation, result in self.results.items():
                file.write(f"{operation}: {result}\n")

# Приклад використання
calculator = VectorCalculator('vector1.txt', 'vector2.txt')

calculator.add()
calculator.subtract()
calculator.multiply()
calculator.divide()

calculator.write_results()
