class VectorCalculator:
    def __init__(self, vector1, vector2):
        self.vec1 = vector1
        self.vec2 = vector2

    @staticmethod
    def read_vectors(filename):
        try:
            with open(filename, 'r') as file:
                lines = file.readlines()
                vector1 = tuple(map(float, lines[0].strip().split(',')))
                vector2 = tuple(map(float, lines[1].strip().split(',')))
            return vector1, vector2
        except FileNotFoundError:
           print("file not found")

    @staticmethod
    def write_vector(filename, vector, operation=None):
        with open(filename, 'a') as file:
            if operation:
                file.write(f"{vector} {operation}\n")
            else:
                file.write(','.join(map(str, vector)) + '\n')

    @staticmethod
    def add_vectors(vec1, vec2):
        result = tuple(x + y for x, y in zip(vec1, vec2))
        return result

    @staticmethod
    def subtract_vectors(vec1, vec2):
        result = tuple(x - y for x, y in zip(vec1, vec2))
        return result

    @staticmethod
    def multiply_vectors(vec1, vec2):
        result = tuple(x * y for x, y in zip(vec1, vec2))
        return result

    @staticmethod
    def divide_vectors(vec1, vec2):
        if any(x == 0 for x in vec2):
            return None
        else:
            result = tuple(x / y for x, y in zip(vec1, vec2))
            return result

    def process_vectors(self, output_file):
        result_addition = self.add_vectors(self.vec1, self.vec2)
        result_multiply = self.multiply_vectors(self.vec1, self.vec2)
        result_subtract = self.subtract_vectors(self.vec1, self.vec2)
        result_divide = self.divide_vectors(self.vec1, self.vec2)

        with open(output_file, 'w') as file:
            self.write_vector(output_file, result_addition, 'addition')
            self.write_vector(output_file, result_subtract, 'subtract')
            self.write_vector(output_file, result_multiply, 'multiply')
            self.write_vector(output_file, result_divide, 'divide')

def main():
    input_file = 'input.txt'
    output_file = 'output.txt'

    vec1, vec2 = VectorCalculator.read_vectors(input_file)
    calculator = VectorCalculator(vec1, vec2)
    calculator.process_vectors(output_file)

if __name__ == "__main__":
    main()
