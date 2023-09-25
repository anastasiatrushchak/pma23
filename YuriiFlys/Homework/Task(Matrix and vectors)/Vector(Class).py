class Vector:
    def __init__(self, vector):
        self.vector = vector

    @classmethod
    def from_file(cls, filename):
        try:
            with open(filename, 'r') as f:
                vector = [float(num) for num in f.readline().split(',')]
            return cls(vector)
        except Exception as e:
            print(f"Error reading vector from file: {e}")
            return None

    def write_vector(self, filename):
        try:
            with open(filename, 'w') as f:
                f.write(', '.join(['{:0.5g}'.format(x) for x in self.vector]) + '\n')
        except Exception as e:
            print(f"Error writing vector to file: {e}")

    def vector_add(self, other_vector):
        if len(self.vector) != len(other_vector):
            print("Error: Vectors must have the same length for addition.")
            return None
        return [self.vector[i] + other_vector[i] for i in range(len(self.vector))]

    def vector_subtract(self, other_vector):
        if len(self.vector) != len(other_vector):
            print("Error: Vectors must have the same length for subtraction.")
            return None
        return [self.vector[i] - other_vector[i] for i in range(len(self.vector))]

    def vector_multiply(self, other_vector):
        if len(self.vector) != len(other_vector):
            print("Error: Vectors must have the same length for multiplication.")
            return None
        return [self.vector[i] * other_vector[i] for i in range(len(self.vector))]

    def vector_divide(self, other_vector):
        try:
            if len(self.vector) != len(other_vector):
                print("Error: Vectors must have the same length for division.")
                return None
            return [self.vector[i] / other_vector[i] for i in range(len(self.vector))]
        except ZeroDivisionError:
            print("Error: Division by zero is not allowed.")
            return None


vector = Vector.from_file('vectors.txt')
other_vector = Vector.from_file('other_vector.txt')
other_vector1= Vector.from_file('other_vector1.txt')
if vector is not None:
    operation = input("Enter operation (add, subtract, multiply, divide): ")


    if operation == 'add':
        result = vector.vector_add(other_vector.vector)
    elif operation == 'subtract':
        result = vector.vector_subtract(other_vector.vector)
    elif operation == 'multiply':
        result = vector.vector_multiply(other_vector.vector)
    elif operation == 'divide':
        result = vector.vector_divide(other_vector.vector)
    else:
        print("Invalid operation")

    if result is not None:
        print(', '.join('{:0.5g}'.format(x) for x in result))
        vector.write_vector('result_vector.txt')
