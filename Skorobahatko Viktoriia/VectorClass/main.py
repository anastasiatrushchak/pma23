class VectorCalculator:
    def __init__(self, input_file, output_file):
        self.input_file = input_file
        self.output_file = output_file

    @staticmethod
    def read_vectors(filename):
        with open(filename, 'r') as file:
            lines = file.readlines()
            vector1 = tuple(map(float, lines[0].strip().split(',')))
            vector2 = tuple(map(float, lines[1].strip().split(',')))
            return vector1, vector2

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
        result = tuple(x / y for x, y in zip(vec1, vec2))
        return result

    def process_vectors(self):
        vector1, vector2 = self.read_vectors(self.input_file)

        with open(self.output_file, 'w') as file:
            result = self.add_vectors(vector1, vector2)
            self.write_vector(self.output_file, result, '+')

            result = self.subtract_vectors(vector1, vector2)
            self.write_vector(self.output_file, result, '-')

            result = self.multiply_vectors(vector1, vector2)
            self.write_vector(self.output_file, result, '*')

            result = self.divide_vectors(vector1, vector2)
            self.write_vector(self.output_file, result, '/')


def main():
    input_file = 'input.txt'
    output_file = 'output.txt'

    calculator = VectorCalculator(input_file, output_file)
    calculator.process_vectors()


if __name__ == "__main__":
    main()
