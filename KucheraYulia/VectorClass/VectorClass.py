import os


def file_exists(filename):
    if os.path.isfile(filename):
        print("Файл існує.")
        with open(filename, 'r') as file:
            if file.read() == "":
                print("Файл порожній.")
            else:
                print("Файл не порожній.")
    else:
        print("Файл не існує.")


class Vector:
    def __init__(self, values):
        self.values = values

    def __str__(self):
        return str(self.values)

    def __add__(self, other):
        if len(self.values) == len(other.values):
            result_values = [x + y for x, y in zip(self.values, other.values)]
            return Vector(result_values)
        else:
            raise ValueError("Вектори мають бути однакової довжини для додавання")

    def __sub__(self, other):
        if len(self.values) == len(other.values):
            result_values = [x - y for x, y in zip(self.values, other.values)]
            return Vector(result_values)
        else:
            raise ValueError("Вектори мають бути однакової довжини для віднімання")

    def __mul__(self, other):
        if len(self.values) == len(other.values):
            result_values = [x * y for x, y in zip(self.values, other.values)]
            return Vector(result_values)
        else:
            raise ValueError("Вектори мають бути однакової довжини для віднімання")

    def __truediv__(self, other):
        if len(self.values) == len(other.values):
            result_values = []
            for x, y in zip(self.values, other.values):
                if y == 0 or y == "0":
                     result_values = ["ZeroDivisionError"]
                else:
                    result_values.append(x / y)
            return Vector(result_values)
        else:
            raise ValueError("Вектори мають бути однакової довжини для віднімання")


file_exists("VectorClass.txt")
file_exists("OutputVC.txt")
vectors = []
with open("VectorClass.txt", 'r') as file:
    for line in file:
        values = [float(x) for x in line.strip().split()]
        vectors.append(Vector(values))

result_vectors = list()
result_vectors.append(vectors[0] + vectors[1])
result_vectors.append(vectors[0] - vectors[1])
result_vectors.append(vectors[0] * vectors[1])
result_vectors.append(vectors[0] / vectors[1])
with open("OutputVC.txt", 'a') as file:
    for result_vector in result_vectors:
        file.write(str(result_vector))
        file.write("\n")

