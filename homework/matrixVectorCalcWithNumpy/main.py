import numpy as np

# TODO: Матриці. Дії: додавання, віднімання, множення , ділення( множення на матрицю в -1 степені)
'''matrix_a = np.random.randint(10, size=(3, 3))
matrix_b = np.random.randint(10, size=(3, 3))

print("Matrix A:\n%s\n\nMatrix B:\n%s\n"%(matrix_a, matrix_b))

print("Choose operation (+,-,/,*): ", end='')

match input():
    case '+':
        print(np.add(matrix_a, matrix_b))
    case '-':
        print(np.subtract(matrix_a, matrix_b))
    case '/':
        print(np.matmul(matrix_a, np.linalg.inv(matrix_b)))
    case '*':
        print(np.matmul(matrix_a, matrix_b))'''

# TODO: Вектор. Ті ж дії. Ділення вектора - ділення поелементно
'''vector_a = np.random.randint(10, size=6)
vector_b = np.random.randint(10, size=6)

print("Vector A:\n%s\n\nVector B:\n%s\n"%(vector_a, vector_b))

print("Choose operation (+,-,/,*,-1): ", end='')

match input():
    case '+':
        print(np.add(vector_a, vector_b))
    case '-':
        print(np.subtract(vector_a, vector_b))
    case '/':
        print(np.divide(vector_a, vector_b))
    case '*':
        print(np.multiply(vector_a, vector_b))'''

# TODO: Матриця клас те ж саме що і просто матриця просто всі дії запихнути в клас
'''class Matrix:
    def __init__(self, size):
        self.matrix = np.zeros((size, size))
        self.input()

    def input(self):
        for rows in range(0, len(self.matrix)):
            for cols in range(0, len(self.matrix[rows])):
                print("Enter [%d][%d] element:" % (rows, cols), end=' ')
                self.matrix[rows][cols] = int(input())
        print()

    def add(self, other):
        return np.add(self.matrix, other.matrix)

    def substract(self, other):
        return np.subtract(self.matrix, other.matrix)

    def divide(self, other):
        return np.matmul(self.matrix, np.linalg.inv(other.matrix))

    def multiply(self, other):
        return np.matmul(self.matrix, other.matrix)


matrix_a = Matrix(3)
matrix_b = Matrix(3)

print(matrix_a.add(matrix_b))'''


# TODO: Вектор клас. Аналогічно
class Vector:
    def __init__(self, size):
        self.vector = np.zeros(size)
        self.input()

    def input(self):
        for el in range(0, len(self.vector)):
            print("Enter [%d] element:" %el, end=' ')
            self.vector[el] = int(input())
        print()

    def add(self, other):
        return np.add(self.vector, other.vector)

    def substract(self, other):
        return np.subtract(self.vector, other.vector)

    def divide(self, other):
        return np.divide(self.vector, other.vector)

    def multiply(self, other):
        return np.multiply(self.vector, other.vector)


vector_a = Vector(7)
vector_b = Vector(7)

print(vector_a.add(vector_b))
