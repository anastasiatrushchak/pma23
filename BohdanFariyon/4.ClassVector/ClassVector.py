VECTOR_FIRST_FILE = 'VectorFirst.txt'
VECTOR_SECOND_FILE = 'VectorSecond.txt'
VECTOR_FILE_RESULT = 'VectorResult.txt'
mode = 'r'
separate = ','

class Vector:
    def __init__(self, vector=[]):
        self.__vector = vector
    def read(self,VECTOR_FILE):
        try:
            with open(VECTOR_FILE, mode) as file:
                vector_first = file.readline().split(separate)
                self.vector = [float(i) for i in vector_first]


        except FileNotFoundError:
            print("File " + VECTOR_FILE + " no found.")
            exit(-1)
    def __add__(self, other):
        try:
            sum = []
            for i in range(max(len(self.vector), len(other.vector))):
                sum.append(self.vector[i] + other.vector[i])
            return sum
        except IndexError:
            print("Dimension vectors cannot be added " + str(len(self.vector)) + " and " + str(len(other.vector)))
            exit(-1)
    def __sub__(self, other):
        try:
            difference = []
            for i in range(max(len(self.vector), len(other.vector))):
                difference.append(self.vector[i] - other.vector[i])
            return difference
        except IndexError:
            print("Dimension vectors cannot be subtracted " + str(len(self.vector)) + " and " + str(len(other.vector)))
            exit(-1)
    def __mul__(self, other):
        try:
            multipliation = []
            for i in range(max(len(self.vector), len(other.vector))):
                multipliation.append(self.vector[i] * other.vector[i])
            return multipliation
        except IndexError:
            print("Dimension vectors cannot be multiplied " + str(len(self.vector)) + " and " + str(len(other.vector)))
            exit(-1)
    def __truediv__(self, other):
        try:
            divide = []
            for i in range(max(len(self.vector), len(other.vector))):
                divide.append(self.vector[i] / other.vector[i])
            return divide
        except IndexError:
            print("Dimension vectors cannot be divided " + str(len(self.vector)) + " and " + str(len(other.vector)))
            exit(-1)
        except ZeroDivisionError:
            print("It is not possible to divide by zero")
            exit(-1)
FirstVector = Vector()
SecondVector = Vector()
FirstVector.read(VECTOR_FIRST_FILE)
SecondVector.read(VECTOR_SECOND_FILE)
sum = FirstVector + SecondVector
difference = FirstVector - SecondVector
multipliation = FirstVector * SecondVector
divide = FirstVector / SecondVector
with open(VECTOR_FILE_RESULT, 'w') as file:
    file.write("Addition:\n" + str(sum)+'\n')
    file.write("Subtraction:\n" + str(difference)+'\n')
    file.write("Multiplication:\n" + str(multipliation) + '\n')
    file.write("Division:\n" + str(divide) + '\n')