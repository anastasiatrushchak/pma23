class Vector:
    def __init__(self, elements):
        self.elements = elements

    def __add__(self, other):
        if len(self.elements) != len(other.elements):
            raise ValueError("Розмірність векторів не співпадає")
        result_elements = [a + b for a, b in zip(self.elements, other.elements)]
        return Vector(result_elements)

    def __sub__(self, other):
        if len(self.elements) != len(other.elements):
            raise ValueError("Розмірність векторів не співпадає")
        result_elements = [a - b for a, b in zip(self.elements, other.elements)]
        return Vector(result_elements)

    def __mul__(self, scalar):
        result_elements = [a * scalar for a in self.elements]
        return Vector(result_elements)

    def __truediv__(self, scalar):
        if scalar == 0:
            raise ValueError("Ділення на нуль неможливе")
        result_elements = [a / scalar for a in self.elements]
        return Vector(result_elements)

    def __str__(self):
        return "(" + ", ".join(map(str, self.elements)) + ")"

class VectorCalculator:
    def __init__(self):
        self.operations = []

    def add_operation(self, operation):
        self.operations.append(operation)

    def execute_operations(self):
        results = []
        for operation in self.operations:
            result = operation()
            results.append(result)
        return results

    def save_operations_to_file(self, file_name):
        with open(file_name, 'w') as file:
            for operation in self.operations:
                file.write(str(operation) + '\n')

# Функція для зчитування векторів з файлу
def read_vector_from_file(file_name):
    with open(file_name, 'r') as file:
        elements = [float(x) for x in file.readline().split(',')]
        return Vector(elements)

# Функція для запису вектора в файл
def write_vector_to_file(vector, file_name):
    with open(file_name, 'w') as file:
        file.write(" ".join(map(str, vector.elements)))

# Зчитуємо вектори з файлів
vector1 = read_vector_from_file('vector1.txt')
vector2 = read_vector_from_file('vector2.txt')

# Створюємо об'єкт калькулятора
vector_calculator = VectorCalculator()

# Додаємо операції до калькулятора
vector_calculator.add_operation(lambda: vector1 + vector2)
vector_calculator.add_operation(lambda: vector1 - vector2)
vector_calculator.add_operation(lambda: vector1 * 2)
vector_calculator.add_operation(lambda: vector2 / 2)

# Виконуємо операції та зберігаємо результати в файл
results = vector_calculator.execute_operations()
vector_calculator.save_operations_to_file('vector_operations.txt')

# Виводимо результати
for i, result in enumerate(results):
    print(f"Операція {i + 1}: {result}")
