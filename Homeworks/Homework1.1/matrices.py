import numpy as np

# vectors to test
# matrixA = np.matrix([[3, 5, 1],
#                      [2, -1, 9],
#                      [1, 0, 6]])
#
# matrixB = np.matrix([[8, 7, 5],
#                      [0, 4, 2],
#                      [-3, 5, 1]])

class Matrix:
    def __init__(self):
        self.matrix = np.zeros((3,3), dtype=int)
        for i in range(3):
            for j in range(3):
                self.matrix[i][j] = int(input(f"Enter the element at position ({i + 1},{j + 1}): "))
    def __str__(self):
        return str(self.matrix)
    def addition(self, other):
        print("Matrices addition:\n", np.add(self.matrix, other.matrix))
    def subtraction(self, other):
        print("Matrices subtraction:\n", np.subtract(self.matrix, other.matrix))
    def multiplication(self, other):
        print("Matrices multiplication:\n", np.matmul(self.matrix, other.matrix))
    def division(self, other):
        try:
            print("Matrices division:\n", self.matrix @ np.linalg.inv(other.matrix))
        except np.linalg.LinAlgError:
            print("Can't do the division of A and B")

matrixA = Matrix()
print(matrixA)
matrixB = Matrix()
print(matrixB)

matrixA.addition(matrixB)
matrixA.subtraction(matrixB)
matrixA.multiplication(matrixB)
matrixA.division(matrixB)

