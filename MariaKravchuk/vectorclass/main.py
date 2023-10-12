class Vector:
    def __init__(self, data=None):
        if data is not None:
            self.data = data
        else:
            self.data = []

    def set_value(self, index, value):
        if 0 <= index < len(self.data):
            self.data[index] = value
        else:
            print("Invalid index")

    def get_value(self, index):
        if 0 <= index < len(self.data):
            return self.data[index]
        else:
            print("Invalid index")

    def __sub__(self, other):
        if len(self.data) != len(other.data):
            print("Vector dimensions do not match for subtraction.")
            return None

        result_minus = [self.data[i] - other.data[i] for i in range(len(self.data))]
        return Vector(result_minus)

    def __add__(self, other):
        if len(self.data) != len(other.data):
            print("Vector dimensions do not match for addition.")
            return None

        result_plus = [self.data[i] + other.data[i] for i in range(len(self.data))]
        return Vector(result_plus)

    def multiplication(self, other):
        if len(self.data) != len(other.data):
            print("Vector dimensions do not match for multiply.")
            return None

        result_multiplication = [self.data[i] * other.data[i] for i in range(len(self.data))]
        return Vector(result_multiplication)
    def division(self, other):
        if len(self.data) != len(other.data):
            print("Vector dimensions do not match for division.")
            return None

        result_division = []
        for i in range(len(self.data)):
            if other.data[i] == 0:
                print(f"Error: Division by zero at index {i}.")
                return None
            result_division.append(self.data[i] / other.data[i])

        return Vector(result_division)

    def __str__(self):
        return "\t".join(map(str, self.data))

    def save_to_file(self, filename):
        try:
            with open(filename, 'w') as file:
                file.write("\t".join(map(str, self.data)) + "\n")
        except Exception as e:
            print(f"Error while saving to file '{filename}': {str(e)}")


def read_vector_from_file(filename):
    try:
        with open(filename, 'r') as file:
            line = file.readline()
            values = list(map(int, line.strip().split()))
            return Vector(values)
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
        return None


first_vector = read_vector_from_file("first_vect.txt")
second_vector = read_vector_from_file("second_vect.txt")

if first_vector and second_vector:
    with open("finish_result.txt", 'w') as result_file:

        result_file.write("First Vector:\n")
        result_file.write(str(first_vector))
        result_file.write("\n\nSecond Vector:\n")
        result_file.write(str(second_vector))
        result_file.write("\n\n")

        result_addition = first_vector + second_vector
        result_subtraction = first_vector - second_vector
        result_multiplication = first_vector.multiplication(second_vector)
        result_division=first_vector.division(second_vector)


        if result_addition:
            result_file.write("Sum:\n")
            result_file.write(str(result_addition))
            result_file.write("\n\n")

        if result_subtraction:
            result_file.write("Difference :\n")
            result_file.write(str(result_subtraction))
            result_file.write("\n\n")

        if result_multiplication is not None:
            result_file.write("Multiplication:\n")
            result_file.write(str(result_multiplication))
            result_file.write("\n\n")

        if result_division is not None:
            result_file.write("Division:\n")
            result_file.write(str(result_division))
            result_file.write("\n\n")


