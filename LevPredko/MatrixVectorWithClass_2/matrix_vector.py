import Constants
class Matrix:
    def __init__(self, file_path1, file_path2):
        self.matrix1 = self.read_matrix_from_file(file_path1)
        self.matrix2 = self.read_matrix_from_file(file_path2)

    @staticmethod
    def read_matrix_from_file(file_path):

        matrix = []
        with open(file_path, 'r') as readFile:
            for line in readFile:
                line = line.strip()
                row = [int(i) for i in line.split(Constants.SEPARATOR)]
                matrix.append(row)
        return matrix

    def additionM(self):
        addition = []
        for i in range(len(self.matrix1)):
            row = []
            for j in range(len(self.matrix1[0])):
                row.append(self.matrix1[i][j] + self.matrix2[i][j])
            addition.append(row)
        return addition

    def subtractionM(self):
        subtraction = []
        for i in range(len(self.matrix1)):
            row = []
            for j in range(len(self.matrix1[0])):
                row.append(self.matrix1[i][j] - self.matrix2[i][j])
            subtraction.append(row)
        return subtraction

    def multiplicationM(self):
        if len(self.matrix1[0]) != len(self.matrix2):
            raise ValueError("The number of columns of the first matrix is not equal to the number of rows of the second matrix")
        multiplication = []
        for i in range(len(self.matrix1)):
            row = []
            for j in range(len(self.matrix2[0])):
                product = 0
                for k in range(len(self.matrix2)):
                    product += self.matrix1[i][k] * self.matrix2[k][j]
                row.append(product)
            multiplication.append(row)
        return multiplication

    def matrix_1(self):
        detB = ((self.matrix2[0][0] * ((self.matrix2[1][1] * self.matrix2[2][2]) - (self.matrix2[1][2] * self.matrix2[2][1]))) -
                (self.matrix2[0][1] * ((self.matrix2[1][0] * self.matrix2[2][0]) - (self.matrix2[1][2] * self.matrix2[2][2]))) +
                (self.matrix2[0][2] * ((self.matrix2[1][0] * self.matrix2[2][1]) - (self.matrix2[1][1] * self.matrix2[2][0]))))

        c11 = "{:.2f}".format(((1 / detB) * ((self.matrix2[1][1] * self.matrix2[2][2]) - (self.matrix2[1][2] * self.matrix2[2][1]))))
        c12 = "{:.2f}".format(-((1 / detB) * ((self.matrix2[1][0] * self.matrix2[2][2]) - (self.matrix2[1][2] * self.matrix2[2][0]))))
        c13 = "{:.2f}".format(((1 / detB) * ((self.matrix2[1][0] * self.matrix2[2][1]) - (self.matrix2[1][1] * self.matrix2[2][0]))))

        c21 = "{:.2f}".format(-((1 / detB) * ((self.matrix2[0][1] * self.matrix2[2][2]) - (self.matrix2[0][2] * self.matrix2[2][1]))))
        c22 = "{:.2f}".format(((1 / detB) * ((self.matrix2[0][0] * self.matrix2[2][2]) - (self.matrix2[0][2] * self.matrix2[2][0]))))
        c23 = "{:.2f}".format(-((1 / detB) * ((self.matrix2[0][0] * self.matrix2[2][1]) - (self.matrix2[0][1] * self.matrix2[2][0]))))

        c31 = "{:.2f}".format(((1 / detB) * ((self.matrix2[0][1] * self.matrix2[1][2]) - (self.matrix2[0][2] * self.matrix2[1][1]))))
        c32 = "{:.2f}".format(-((1 / detB) * ((self.matrix2[0][0] * self.matrix2[1][2]) - (self.matrix2[0][2] * self.matrix2[1][0]))))
        c33 = "{:.2f}".format(((1 / detB) * ((self.matrix2[0][0] * self.matrix2[1][1]) - (self.matrix2[0][1] * self.matrix2[1][0]))))

        matrix_1 = [
            [c11, c12, c13],
            [c21, c22, c23],
            [c31, c32, c33]
        ]
        return matrix_1

    def divideM(self, matrix2T):
        if len(self.matrix1[0]) != len(matrix2T):
            raise ValueError(
                "The number of columns of the first matrix is not equal to the number of rows of the second matrix")
        divide = []
        for i in range(len(self.matrix1)):
            row = []
            for j in range(len(matrix2T[0])):
                product = 0
                for k in range(len(matrix2T)):
                    product += float(self.matrix1[i][k]) * float(matrix2T[k][j])
                row.append("{:.2f}".format(product))
            divide.append(row)
        return divide


class Vector:
    def __init__(self, file_path1, file_path2):
        self.vector1 = self.read_vector_from_file(file_path1)
        self.vector2 = self.read_vector_from_file(file_path2)

    @staticmethod
    def read_vector_from_file(file_path):
        vector = []
        with open(file_path, 'r') as readFile:
            for line in readFile: # цикл прочитує кожну строку з файлу і опрацьовує її
                line = line.strip() #видаляє всі лишні пробіли
                row = [int(i) for i in line.split(Constants.SEPARATOR)] # розбиває рядок на окермі елементи які йдуть через SEPARATOR
                vector.append(row) #кожен рядок файлу стає елементом списку vector
        return vector

    def additionV(self):
        if len(self.vector1) != len(self.vector2):
            raise ValueError("The vectors must have the same length")
        add_vector = []
        for i in range(len(self.vector1)):
            result_row = []
            for j in range(len(self.vector1[i])):
                result_row.append(self.vector1[i][j] + self.vector2[i][j])
            add_vector.append(result_row)
        return add_vector

    def subtractionV(self):
        if len(self.vector1) != len(self.vector2):
            raise ValueError("The vectors must have the same length")
        sub_vector = []
        for i in range(len(self.vector1)):
            result_row = []
            for j in range(len(self.vector1[i])):
                result_row.append(self.vector1[i][j] - self.vector2[i][j])
            sub_vector.append(result_row)
        return sub_vector
    def multiplicationV(self):
        if len(self.vector1) != len(self.vector2):
            raise ValueError("The vectors must have the same length")
        mul_vector = []
        for i in range(len(self.vector1)):
            result_row = []
            for j in range(len(self.vector1[i])):
                result_row.append(self.vector1[i][j] * self.vector2[i][j])
            mul_vector.append(result_row)
        return mul_vector

    def divideV(self):
        if len(self.vector1) != len(self.vector2):
            raise ValueError("The vectors must have the same length")
        div_vector = []
        for i in range(len(self.vector1)):
            result_row = []
            for j in range(len(self.vector1[i])):
                if self.vector2[i][j] == 0:
                    raise ValueError("Division by zero is not allowed")
                result_row.append(self.vector1[i][j] / self.vector2[i][j])
            div_vector.append(result_row)
        return div_vector


matrix = Matrix(Constants.Input_Matrix_1, Constants.Input_Matrix_2)
vector = Vector(Constants.Input_Vector_1, Constants.Input_Vector_2)

with open("output.txt", "w") as file:
    choice = input("Matrix or Vector? (M or V): ")
    operation = input("Enter the operation (+, -, *, /): ")

    if choice == "M":
        if operation == "+":
            result = matrix.additionM()
        elif operation == "-":
            result = matrix.subtractionM()
        elif operation == "*":
            result = matrix.multiplicationM()
        elif operation == "/":
            matrix2T = matrix.matrix_1()
            result = matrix.divideM(matrix2T)
        else:
            raise ValueError("There is no such operator for matrices")

        for row in result:
            file.write(' '.join(map(str, row)) + '\n')
    elif choice == "V":
        if operation == "+":
             result = vector.additionV()
        elif operation == "-":
            result = vector.subtractionV()
        elif operation == "*":
            result = vector.multiplicationV()
        elif operation == "/":
            result = vector.divideV()
        else:
               raise ValueError("There is no such operator for vectors")

        for item in result:
            file.write(str(item) + '\n')
    else:
        raise ValueError("Invalid choice.")
