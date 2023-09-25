import const


class Vector:
    def __init__(self, array):
        self.array = array

    def __add__(self, other):
        result = []
        for i in range(len(self.array)):
            result.append(self.array[i] + other.array[i])
        return result

    def __sub__(self, other):
        result = []
        for i in range(len(self.array)):
            result.append(self.array[i] - other.array[i])
        return result

    def __truediv__(self, other):
        result = []
        try:
            for i in range(len(self.array)):
                result.append(self.array[i] / other.array[i])
            return result
        except ZeroDivisionError:
            print(const.ZERO_DIVISION)
            exit(-1)

    def __mul__(self, other):
        result = []
        for i in range(len(self.array)):
            result.append(self.array[i] * other.array[i])
        return result

    @staticmethod
    def read(file_name):
        try:
            with open(file_name, 'r') as inpV:
                vect = inpV.readline().split()
                vect = [float(i) for i in vect if i.isdigit()]
        except FileNotFoundError:
            print(const.FILE_NOT_FOUND)
            exit(-1)
        return Vector(vect)
    @staticmethod
    def write(vector1, vector2, file_name):
        with open(file_name, 'w') as out:
            out.write("Addition:\n")
            out.write(str(vector1 + vector2) + '\n')

            out.write("Subtraction:\n")
            out.write(str(vector1 - vector2) + '\n')

            out.write("Multiplication:\n")
            out.write(str(vector1 * vector2) + '\n')

            out.write("Division:\n")
            out.write(str(vector1 / vector2) + '\n')

