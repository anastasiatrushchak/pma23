import os

VECTOR_ONE_FILE = "vector_one.txt"
VECTOR_TWO_WILE = "vector_two.txt"
RESULT_FILE = "calculating_result.txt"
NEW_VECTOR = "new_vector.txt"

class FileException(Exception):
    pass


def read_file(filename):
    try:
        if not os.path.exists(filename):
            raise FileException("Error!", filename, " is not found!")
        with open(filename) as file:
            line = file.readline().split()
            line = [float(i) for i in line if i.isdigit]
            return line
    except FileException as file_err:
        print(file_err)


def push_to_file(vector):
    try:
        if len(vector) == 0:
            raise Exception("Error! Vector is empty")
        with open(RESULT_FILE, "w") as file:
            file.write(str(vector))
    except Exception as err:
        print(err)


class Vector:
    def __init__(self, vector=[]):
        self.vector = vector

    def __add__(self, other):
        try:
            if len(self.vector) != len(other.vector):
                raise Exception("Error! The lengths of vectors are not equal!")
            vector = [self.vector[i] + other.vector[i] for i in range(len(self.vector))]
            return vector
        except Exception as err:
            print(err)

    def __sub__(self, other):
        try:
            if len(self.vector) != len(other.vector):
                raise Exception("Error! The lengths of vectors are not equal!")
            vector = [self.vector[i] - other.vector[i] for i in range(len(self.vector))]
            return vector
        except Exception as err:
            print(err)

    def __mul__(self, other):
        try:
            if len(self.vector) != len(other.vector):
                raise Exception("Error! The lengths of vectors are not equal!")
            vector = [self.vector[i] * other.vector[i] for i in range(len(self.vector))]
            return vector
        except Exception as err:
            print(err)

    def __truediv__(self, other):
        try:
            if len(self.vector) != len(other.vector):
                raise Exception("Error! The lengths of vectors are not equal!")
            if 0 in other.vector:
                raise Exception("Error! Dividing by zero!")
            vector = [self.vector[i] / other.vector[i] for i in range(len(self.vector))]
            return vector
        except Exception as err:
            print(err)


a = Vector(read_file(VECTOR_ONE_FILE))
b = Vector(read_file(VECTOR_TWO_WILE))
new_vec = Vector(read_file(NEW_VECTOR))
vector_summing = Vector(a+b)
push_to_file(vector_summing+new_vec)