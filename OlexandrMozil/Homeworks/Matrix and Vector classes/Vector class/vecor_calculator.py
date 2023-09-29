import os
import exceptions as exc


class Vector:
    def __init__(self):
        self.vector = []
        self.filename = ""

    def __len__(self):
        return len(self.vector)

    def __getitem__(self, index):
        return self.vector[index]
    
    def __add__(self, other):
        return self.addition(self.vector, other.vector)

    def __sub__(self, other):
        return self.subtraction(self.vector, other.vector)

    def __mul__(self, other):
        return self.multiplication(self.vector, other.vector)

    def __truediv__(self, other):
        return self.division(self.vector, other.vector)

    def addition(self, vector1, vector2):
        result = []
        for i in range(len(vector1)):
            result.append(vector1[i] + vector2[i])
        return result

    def subtraction(self, vector1, vector2):
        result = []
        for i in range(len(vector1)):
            result.append(vector1[i] - vector2[i])
        return result

    def multiplication(self, vector1, vector2):
        result = []
        for i in range(len(vector1)):
            result.append(vector1[i] * vector2[i])
        return result

    def division(self, vector1, vector2):
        try:
            result = []
            for i in range(len(vector1)):
                result.append(vector1[i] / vector2[i])
            return result
        except ZeroDivisionError:
            print("Division by zero!")
            raise SystemExit

    def load_vector(self):
        try:
            self.filename = input("Input name of the file with vector (0 for result vector): ") + ".txt"
            if os.path.exists(self.filename):
                with open(self.filename, "r") as readFile:
                    if os.path.getsize(self.filename) == 0:
                        raise exc.EmptyFile("File is empty!")
                    else:
                        self.vector = [float(number) for line in readFile for number in line.split()]
            else:
                raise exc.FileDoesntExist("No input file was found!")
        except exc.FileDoesntExist as FDE:
            print(FDE)
            raise SystemExit
        except exc.EmptyFile as EF:
            print(EF)
            raise SystemExit

    def form_zero_vector(self, other):
        for i in range(len(other)):
            self.vector.append(0)

    def save_result(self, vector1, vector2):
        # summ = self.addition(vector1, vector2)
        # subtraction = self.subtraction(vector1, vector2)
        # multiplication = self.multiplication(vector1, vector2)
        # division = self.division(vector1, vector2)
        summ = a+b
        subtraction = a-b
        multiplication = a*b
        division = a/b
        output_string = (f"Сума:\n{summ}\n\n"
                         f"Різниця:\n{subtraction}"
                         f"\n\nДобуток:\n{multiplication}\n\n"
                         f"Частка:\n{division}")

        with open("result_vectors.txt", "w") as writeFile:
            writeFile.write(output_string)


a = Vector()
a.load_vector()
b = Vector()
b.load_vector()
result = Vector()
result.form_zero_vector(a)
result.save_result(a, b)
# print("\n", a / b)

