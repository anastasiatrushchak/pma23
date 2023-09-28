import os
import exceptions as exc
import additional_func as adfunc


class Matrix:
    def __init__(self, size=3):
        try:
            self.filename = input("Input name of the file with matrix: ") + ".txt"
            self.matrix = []
            if os.path.exists(self.filename):
                with open(self.filename, "r") as readFile:
                    if os.path.getsize(self.filename) == 0:
                        raise exc.EmptyFile("File is empty!")
                    else:
                        self.matrix = [[float(num) for num in line.split(' ')] for line in readFile]
                        self.size = len(self.matrix)
            else:
                raise exc.FileDoesntExist("No input file was found!")
        except exc.FileDoesntExist as FDE:
            print(FDE)
            self.size = size
            self.matrix = adfunc.zero_matrix(size)

        except exc.EmptyFile as EF:
            print(EF)
            self.size = size
            self.matrix = adfunc.zero_matrix(size)

    def __len__(self):
        return self.size

    def __getitem__(self, index):
        return self.matrix[index]

    def __add__(self, other):
        return self.summ(self.matrix, other.matrix)

    def __sub__(self, other):
        return self.subtraction(self.matrix, other.matrix)

    def __mul__(self, other):
        return self.multiplication(self.matrix, other.matrix)

    def __truediv__(self, other):
        return self.division(self.matrix, other.matrix)

    def summ(self, matrix1, matrix2):
        summ = adfunc.zero_matrix(len(matrix1))
        for i in range(len(matrix1)):
            for j in range(len(matrix1[0])):
                summ[i][j] = matrix1[i][j] + matrix2[i][j]
        return summ

    def subtraction(self, matrix1, matrix2):
        subtraction = adfunc.zero_matrix(len(matrix1))
        for i in range(len(matrix1)):
            for j in range(len(matrix1[0])):
                subtraction[i][j] = matrix1[i][j] - matrix2[i][j]
        return subtraction

    def multiplication(self, matrix1, matrix2):
        multiplication = adfunc.zero_matrix(len(matrix1))
        for i in range(len(matrix1)):
            for j in range(len(matrix2[0])):
                for k in range(len(matrix2)):
                    multiplication[i][j] += matrix1[i][k] * matrix2[k][j]
        return multiplication

    def division(self, matrix1, matrix2):
        try:
            prepared_matrix = adfunc.get_cofactor_matrix(matrix2)
            prepared_matrix = adfunc.transpose(prepared_matrix)
            prepared_matrix = adfunc.multiplication_by_number(prepared_matrix, 1 / (adfunc.get_determinant(matrix2)))
            return self.multiplication(matrix1, prepared_matrix)
        except ZeroDivisionError:
            print("Division by zero!")
            raise SystemExit

    def save_result(self, matrix1, matrix2):
        summ = self.summ(matrix1, matrix2)
        subtraction = self.subtraction(matrix1, matrix2)
        multiplication = self.multiplication(matrix1, matrix2)
        division = self.division(matrix1, matrix2)
        output_string = (f"Сума:\n{adfunc.matrix_to_string(summ)}\n\n"
                         f"Різниця:\n{adfunc.matrix_to_string(subtraction)}"
                         f"\n\nДобуток:\n{adfunc.matrix_to_string(multiplication)}\n\n"
                         f"Частка:\n{adfunc.matrix_to_string(division)}")

        with open("result_matrices.txt", "w") as writeFile:
            writeFile.write(output_string)


a = Matrix()
b = Matrix()
result = Matrix()

print("Matrix A:")
print(adfunc.matrix_to_string(a.matrix))
print("\nMatrix B:")
print(adfunc.matrix_to_string(b.matrix))

print("\n", adfunc.matrix_to_string(a / b))

result.save_result(a, b)
