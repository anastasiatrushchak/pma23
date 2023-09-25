class VectorOperations:
    def __init__(self, *input_vector_files):
        self.input_vector_files = input_vector_files
        self.vectors = [self.read_vector(filename) for filename in input_vector_files]

    def read_vector(self, filename):
        try:
            vector = []
            with open(filename, "r") as file_vector:
                for line in file_vector:
                    values = line.strip().split()
                    for value in values:
                        vector.append(int(value))
            return vector
        except FileNotFoundError:
            print("File " + filename + " not found")
            exit(-1)

    def sum_vectors(self):
        result_vector = [0] * len(self.vectors[0])  # Initialize with zeros
        for vector in self.vectors:
            result_vector = [i + j for i, j in zip(result_vector, vector)]
        return result_vector

    def subtract_vectors(self):
        result_vector = self.vectors[0][:]
        for vector in self.vectors[1:]:
            result_vector = [i - j for i, j in zip(result_vector, vector)]
        return result_vector

    def multiply_vectors(self):
        result_vector = self.vectors[0][:]
        for vector in self.vectors[1:]:
            result_vector = [i * j for i, j in zip(result_vector, vector)]
        return result_vector

    def divide_vectors(self):
        try:
            result_vector = self.vectors[0][:]
            for vector in self.vectors[1:]:
                result_vector = [i / j for i, j in zip(result_vector, vector)]
            return result_vector
        except ZeroDivisionError:
            print("Cannot divide by zero")
            exit(-1)

    def write_results(self):
        sum_result = self.sum_vectors()
        subtract_result = self.subtract_vectors()
        multiply_result = self.multiply_vectors()
        divide_result = self.divide_vectors()

        with open("output.txt", "w") as f:
            f.write("Sum Result:\n")
            f.write(" ".join(map(str, sum_result)) + "\n")

            f.write("Subtraction Result:\n")
            f.write(" ".join(map(str, subtract_result)) + "\n")

            f.write("Multiplication Result:\n")
            f.write(" ".join(map(str, multiply_result)) + "\n")

            f.write("Division Result:\n")
            f.write(" ".join(map(str, divide_result)) + "\n")


if __name__ == "__main__":
    INPUT_VECTOR_first = "inputVector1.txt"
    INPUT_VECTOR_second = "inputVector2.txt"
    INPUT_VECTOR_third = "inputVector3.txt"  # Add more input vectors as needed

    vector_operations = VectorOperations(INPUT_VECTOR_first, INPUT_VECTOR_second, INPUT_VECTOR_third)
    vector_operations.write_results()
