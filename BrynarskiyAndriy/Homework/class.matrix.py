class Matrix: 
    def __init__(self, rows, columns): 
        self.rows = rows 
        self.columns = columns 
        self.data = [[0 for _ in range(columns)] for _ in range(rows)] 
 
    def set_element(self, row, column, value): 
        if 0 <= row < self.rows and 0 <= column < self.columns: 
            self.data[row][column] = value 
        else: 
            raise ValueError("Неправильні індекси") 
 
    def get_element(self, row, column): 
        if 0 <= row < self.rows and 0 <= column < self.columns: 
            return self.data[row][column] 
        else: 
            raise ValueError("Неправильні індекси") 
 
    def __add__(self, other): 
        if self.rows != other.rows or self.columns != other.columns: 
            raise ValueError("Розмірності матриць не співпадають") 
 
        result = Matrix(self.rows, self.columns) 
        for i in range(self.rows): 
            for j in range(self.columns): 
                result.set_element(i, j, self.get_element(i, j) + other.get_element(i, j)) 
        return result 
 
    def __sub__(self, other): 
        if self.rows != other.rows or self.columns != other.columns: 
            raise ValueError("Розмірності матриць не співпадають") 
 
        result = Matrix(self.rows, self.columns) 
        for i in range(self.rows): 
            for j in range(self.columns): 
                result.set_element(i, j, self.get_element(i, j) - other.get_element(i, j)) 
        return result 
 
    def __mul__(self, scalar): 
        result = Matrix(self.rows, self.columns) 
        for i in range(self.rows): 
            for j in range(self.columns): 
                result.set_element(i, j, self.get_element(i, j) * scalar) 
        return result 
 
    def __str__(self): 
        matrix_str = "" 
        for row in self.data: 
            matrix_str += " ".join(map(str, row)) + "\n" 
        return matrix_str 
 
class MatrixCalculator: 
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
 
# Функція для зчитування матриці з файлу 
def read_matrix_from_file(file_name): 
    with open(file_name, 'r') as file: 
        lines = file.readlines() 
        rows = len(lines) 
        columns = len(lines[0].strip().split(",")) 
        matrix = Matrix(rows, columns) 
        for i, line in enumerate(lines): 
            elements = [float(x) for x in line.strip().split(',')] 
            for j, element in enumerate(elements): 
                matrix.set_element(i, j, element) 
        return matrix 
 
# Функція для запису матриці в файл 
def write_matrix_to_file(matrix, file_name): 
    with open(file_name, 'w') as file: 
        for i in range(matrix.rows): 
            row = [str(matrix.get_element(i, j)) for j in range(matrix.columns)] 
            file.write(" ".join(row) + '\n') 
 
# Зчитуємо матриці з файлів 
matrix1 = read_matrix_from_file('matrix1.txt') 
matrix2 = read_matrix_from_file('matrix2.txt') 
 
# Створюємо об'єкт калькулятора 
matrix_calculator = MatrixCalculator() 
 
# Додаємо операції до калькулятора 
matrix_calculator.add_operation(lambda: matrix1 + matrix2) 
matrix_calculator.add_operation(lambda: matrix1 - matrix2) 
matrix_calculator.add_operation(lambda: matrix1 * 2)
matrix_calculator.add_operation(lambda: matrix1 / 2)
 
# Виконуємо операції та зберігаємо результати в файл 
results = matrix_calculator.execute_operations() 
for i, result in enumerate(results): 
    write_matrix_to_file(result, f'result_matrix_{i + 1}.txt') 
 
# Виводимо результати 
for i, result in enumerate(results): 
    print(f"Результат операції {i + 1}:\n{result}")
