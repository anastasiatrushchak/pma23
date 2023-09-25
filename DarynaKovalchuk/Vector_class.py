class DetIsZero(Exception):
    def init(self, message="vector is zero"):
        self.message = message
        super().init(self.message)

class VectorOperations:
    def init(self, first_vector, second_vector):
        self.first_vector = first_vector
        self.second_vector = second_vector

    def add_vectors(self):
        return [x + y for x, y in zip(self.first_vector, self.second_vector)]

    def subtract_vectors(self):
        return [x - y for x, y in zip(self.first_vector, self.second_vector)]

    def multiply_vectors(self):
        return [x * y for x, y in zip(self.first_vector, self.second_vector)]

    def divide_vectors(self):
        return [x / y for x, y in zip(self.first_vector, self.second_vector)]


    def add(self, other):
        return [x + y for x, y in zip(self.first_vector, other.second_vector)]

    def sub(self, other):
        return [x - y for x, y in zip(self.first_vector, other.second_vector)]

    def mul(self, other):
        return [x * y for x, y in zip(self.first_vector, other.second_vector)]

    def truediv(self, other):
        if any(y == 0 for y in other.second_vector):
            raise DetIsZero("division by zero")
        return [x / y for x, y in zip(self.first_vector, other.second_vector)]

def read_vectors_from_file(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            if len(lines) < 2:
                raise Exception("file is empty")
            first_vector = [float(x) for x in lines[0].split()]
            vector2 = [float(x) for x in lines[1].split()]
        return first_vector, vector2
    except FileNotFoundError:
        raise Exception("file not found")
    except Exception as e:
        print(e)
        return None, None

input_filename = 'input.txt'
output_filename = 'output.txt'
first_vector, second_vector = read_vectors_from_file(input_filename)

if first_vector is not None and second_vector is not None:
    vector_operations = VectorOperations(first_vector, second_vector)

    try:
        result_addition = vector_operations + vector_operations
        result_subtract = vector_operations - vector_operations
        result_multiply = vector_operations * vector_operations
        result_divide = vector_operations / vector_operations


        print("addition:", result_addition)
        print("subtract:", result_subtract)
        print("multiply:", result_multiply)
        print("divide:", result_divide)

        with open(output_filename, 'a') as file:
            file.write("addition: {}\n".format(result_addition))
            file.write("subtract: {}\n".format(result_subtract))
            file.write("multiply: {}\n".format(result_multiply))
            file.write("divide: {}\n".format(result_divide))
    except DetIsZero as e:
        print(e)
