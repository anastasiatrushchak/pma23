import constants

with open(constants.INPUT_FILE, 'r') as file:
    line = file.readline()
    vector_a = line.strip().split(constants.SEPARATOR)
    line = file.readline()
    vector_b = line.strip().split(constants.SEPARATOR)

vector_a = [float(i) for i in vector_a]
vector_b = [float(i) for i in vector_b]

print("Vector A:", vector_a)
print("Vector B:", vector_b)


class Vector:

    def __init__(self, vector):
        self.vector = vector

    def __add__(self, vector_b):
        return self.add(vector_b)

    def __sub__(self, vector_b):
        return self.sub(vector_b)

    def __mul__(self, vector_b):
        return self.multiply(vector_b)

    def __truediv__(self, vector_b):
        return self.divide(vector_b)

    def add(self, vector_b):
        vector_c = []
        for i in range(len(vector_b)):
            vector_c.append(self.vector[i] + vector_b[i])
        return vector_c

    def sub(self, vector_b):
        vector_c = []
        for i in range(len(vector_b)):
            vector_c.append(self.vector[i] - vector_b[i])
        return vector_c

    def multiply(self, vector_b):
        vector_c = []
        for i in range(len(vector_b)):
            vector_c.append(self.vector[i] * vector_b[i])
        return vector_c

    def divide(self, vector_b):
        vector_c = []
        for i in range(len(vector_b)):
            try:
                vector_c.append(self.vector[i] / vector_b[i])
            except ZeroDivisionError as e:
                print("Can't divide by zero!")
                vector_c.append(0)
        return vector_c


vector_a = Vector(vector_a)

with open(constants.OUTPUT_FILE, 'w') as file:
    file.writelines("Addition:\n" + str(vector_a + vector_b) + '\n')
    file.writelines("Subtraction:\n" + str(vector_a - vector_b) + '\n')
    file.writelines("Multiplication:\n" + str(vector_a * vector_b) + '\n')
    file.writelines("Division:\n" + str(vector_a / vector_b) + '\n')
