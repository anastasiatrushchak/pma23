VECTOR_FIRST_FILE = 'First_vector.txt'
VECTOR_SECOND_FILE = 'Second_vector.txt'
VECTOR_FILE_RESULT = 'Result.txt'
mode = 'r'
separate = ','

class Vector:
    def __init__(self, vector=[]):
        self.__vector = vector

    def read(self, VECTOR_FILE):
        try:
            with open(VECTOR_FILE, mode) as file:
                vector_first = file.readline().split(separate)
                self.__vector = [float(i) if i.strip() else 0.0 for i in vector_first]

        except FileNotFoundError:
            print("File " + VECTOR_FILE + " not found.")
            exit(-1)

    def __add__(self, other):
        try:
            result = [x + y for x, y in zip(self.__vector, other.__vector)]
            return Vector(result)
        except IndexError:
            print("Dimension vectors cannot be added " + str(len(self.__vector)) + " and " + str(len(other.__vector)))
            exit(-1)

    def __sub__(self, other):
        try:
            result = [x - y for x, y in zip(self.__vector, other.__vector)]
            return Vector(result)
        except IndexError:
            print("Dimension vectors cannot be subtracted " + str(len(self.__vector)) + " and " + str(len(other.__vector)))
            exit(-1)

    def __mul__(self, other):
        try:
            result = [x * y for x, y in zip(self.__vector, other.__vector)]
            return Vector(result)
        except IndexError:
            print("Dimension vectors cannot be multiplied " + str(len(self.__vector)) + " and " + str(len(other.__vector)))
            exit(-1)

    def __truediv__(self, other):
        try:
            result = [x / y for x, y in zip(self.__vector, other.__vector)]
            return Vector(result)
        except IndexError:
            print("Dimension vectors cannot be divided " + str(len(self.__vector)) + " and " + str(len(other.__vector)))
            exit(-1)
        except ZeroDivisionError:
            print("It is not possible to divide by zero")
            exit(-1)

FirstVector = Vector()
SecondVector = Vector()
FirstVector.read(VECTOR_FIRST_FILE)
SecondVector.read(VECTOR_SECOND_FILE)

sum_result = FirstVector + SecondVector
difference_result = FirstVector - SecondVector
multiplication_result = FirstVector * SecondVector
division_result = FirstVector / SecondVector

with open(VECTOR_FILE_RESULT, 'w') as file:
    file.write("Addition:\n" + str(sum_result._Vector__vector) + '\n')
    file.write("Subtraction:\n" + str(difference_result._Vector__vector) + '\n')
    file.write("Multiplication:\n" + str(multiplication_result._Vector__vector) + '\n')
    file.write("Division:\n" + str(division_result._Vector__vector) + '\n')


