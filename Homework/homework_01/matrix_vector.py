import numpy as np

class Matrix:
    def __init__(self): #конструктор
        #зберігання матриць як атрибута обєкта :
        self.matrix1 = np.loadtxt("inputMatrix1.txt", dtype='i', delimiter=' ')
        self.matrix2 = np.loadtxt("inputMatrix2.txt", dtype='i', delimiter=' ')

    def perform_operation(self, operation):
        if operation == '+':
            return self.matrix1 + self.matrix2
        elif operation == '-':
            return self.matrix1 - self.matrix2
        elif operation == '*':
            return np.dot(self.matrix1, self.matrix2)
        elif operation == '/':
            return np.divide(self.matrix1, self.matrix2)
        elif operation == "*'":
            if np.linalg.det(self.matrix2) != 0: #перевірка чи визначник матриці не 0
                matrix2T = np.linalg.inv(self.matrix2) #метод шукає матрицю в -1
                return np.dot(self.matrix1, matrix2T)
            else:
                print("In the matrix you entered, the determinant is 0, so choose another operation")
                return None
        else:
            print("Invalid operation")
            return None

    def save_result(self, result_filename, result):
        if result is not None:
            np.savetxt(result_filename, result, fmt='%d') # формат тільки цілі числа


class Vector:
    def __init__(self):
        self.vector1 = np.loadtxt("inputVector1.txt", dtype='i', delimiter=' ')
        self.vector2 = np.loadtxt("inputVector2.txt", dtype='i', delimiter=' ')

    def perform_operation(self, operation):
        if operation == '+':
            return self.vector1 + self.vector2
        elif operation == '-':
            return self.vector1 - self.vector2
        elif operation == '*':
            return self.vector1 * self.vector2
        elif operation == '/':
            return self.vector1 / self.vector2
        else:
            print("Invalid operation")
            return None

    def save_result(self, result_filename, result):
        if result is not None:
            np.savetxt(result_filename, result, fmt='%d')


def main():
    choice = input("Matrix or Vector? (M or V):")
    result_filename = "output.txt"

    if choice == 'M':
        matrix = Matrix()
        operation = input("Enter the operation (+, -, *, /, *'): ")
        result = matrix.perform_operation(operation)
        matrix.save_result(result_filename, result)

    elif choice == 'V':
        vector = Vector()
        operation = input("Enter the operation (+, -, *, /): ")
        result = vector.perform_operation(operation)
        vector.save_result(result_filename, result)

    else:
        print("Invalid choice")
if __name__ == "__main__":  #відбувається перевірка, чи код виконується  як головний програмний модуль
    main()