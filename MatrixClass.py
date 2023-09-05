class MatrixOperations:
    def __init__(self, X, Y): #конструктор лего
        self.X = X
        self.Y = Y
        self.result = [[0] * len(X[0]) for _ in range(len(X))]

    def add_matrices(self):
        for i in range(len(self.X)):
            for j in range(len(self.X[0])):
                self.result[i][j] = self.X[i][j] + self.Y[i][j]

    def subtract_matrices(self):
        for i in range(len(self.X)):
            for j in range(len(self.X[0])):
                self.result[i][j] = self.X[i][j] - self.Y[i][j]

    def multiply_matrices(self):
        for i in range(len(self.X)):
            for j in range(len(self.Y[0])):
                for k in range(len(self.Y)):
                    self.result[i][j] += self.X[i][k] * self.Y[k][j]

    def print_result(self, operation):
        print(operation)
        for r in self.result:
            print(r)

X = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

Y = [[9, 8, 7],
     [6, 5, 4],
     [3, 2, 1]]

matrix_operations = MatrixOperations(X, Y)

operation = input()
if operation == "add":
    matrix_operations.add_matrices()
    matrix_operations.print_result("add")
if operation == "sub":
    matrix_operations.subtract_matrices()
    matrix_operations.print_result("subtract")
if operation == "mult":
    matrix_operations.multiply_matrices()
    matrix_operations.print_result("multiply")
