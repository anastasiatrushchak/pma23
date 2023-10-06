class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    @staticmethod
    def add(vec1, vec2):
        return Vector(vec1.x + vec2.x, vec1.y + vec2.y, vec1.z + vec2.z)

    @staticmethod
    def subtract(vec1, vec2):
        return Vector(vec1.x - vec2.x, vec1.y - vec2.y, vec1.z - vec2.z)

    @staticmethod
    def multiply(vec1, vec2):
        return Vector(vec1.x * vec2.x, vec1.y * vec2.y, vec1.z * vec2.z)

    @staticmethod
    def divide(vec1, vec2):
        return Vector(vec1.x / vec2.x, vec1.y / vec2.y, vec1.z / vec2.z)

    def __str__(self):
        return f"({self.x},{self.y},{self.z})"

    @staticmethod
    def read_from_file(filename):
        with open(filename, 'r') as file:
            line = file.readline().strip()
            x, y, z = map(int, line.split(','))
        return Vector(x, y, z)

    @staticmethod
    def write_to_file(filename, vector):
        with open(filename, 'a') as file:
            file.write(str(vector) + '\n')


vectorA = Vector.read_from_file('vectorA.txt')
vectorB = Vector.read_from_file('vectorB.txt')

result_add = Vector.add(vectorA, vectorB)
result_subtract = Vector.subtract(vectorA, vectorB)
result_multiply = Vector.multiply(vectorA, vectorB)
result_divide = Vector.divide(vectorA, vectorB)

Vector.write_to_file('result.txt', result_add)
Vector.write_to_file('result.txt', result_subtract)
Vector.write_to_file('result.txt', result_multiply)
Vector.write_to_file('result.txt', result_divide)
