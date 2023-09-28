ZERO_DIVISION_ERROR = 'division by zero'
FILE_NOT_FOUND_ERROR = 'No such file or directory'

class Vector:
    def __init__(self, vector):
        self.vector = vector

    def __add__(self, other):
        result = []
        for i in range(len(self.vector)):
            result.append(self.vector[i] + other.vector[i])
        return result

    def __sub__(self, other):
        result = []
        for i in range(len(self.vector)):
            result.append(self.vector[i] + other.vector[i])
        return result

    def __mul__(self, other):
        result = []
        for i in range(len(self.vector)):
            result.append(self.vector[i] * other.vector[i])
        return result

    def __truediv__(self, other):
        result = []
        for i in range(len(self.vector)):
            result.append(self.vector[i] / other.vector[i])
        return result

    def read(file_name):
        try:
            with open(file_name, 'r') as file:
                line = file.readline().split()
                vector = [float(num) for num in line]
            return Vector(vector)
        except FileNotFoundError:
            print(FILE_NOT_FOUND_ERROR)
            exit(-1)


    def write(filename, text, vector):
        try:
            with open(filename, 'a') as file:
                file.write(text)
                file.write(str(vector))
                file.write("\n")
        except FileNotFoundError:
            print(FILE_NOT_FOUND_ERROR)
            exit(-1)
