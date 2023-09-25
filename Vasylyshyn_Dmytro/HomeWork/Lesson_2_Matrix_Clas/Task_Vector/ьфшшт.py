class Vector:
    def __init__(self, first_vector, second_vector):
        self.first_vector = first_vector
        self.second_vector = second_vector

    def perform_operations(self):
        sum_result = [a + b for a, b in zip(self.first_vector, self.second_vector)]
        subtraction_result = [a - b for a, b in zip(self.first_vector, self.second_vector)]
        division_result = [a / b for a, b in zip(self.first_vector, self.second_vector)]
        multiplication_result = [a * b for a, b in zip(self.first_vector, self.second_vector)]

        return sum_result, subtraction_result, division_result, multiplication_result

def write_data(file_name, results):
    try:
        with open(file_name, 'a') as file:
            for result in results:
                file.write(str(result))
                file.write('\n')
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")
def read_data(file_name):
    try:
        with open(file_name, 'r') as data:
            vector = data.readline().split()

        vector = [float(x) for x in vector]
        return vector
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")
    except ValueError as e:
        print(f"Oops, sorry, but you must write a number: {e}")


from typing import Final

name_input_numbers_first_file: Final[str] = 'first_vector.txt'
name_input_numbers_second_file: Final[str] = 'second_vector.txt'
name_output_file: Final[str] = 'output_vector.txt'

first_vector = read_data(name_input_numbers_first_file)
second_vector = read_data(name_input_numbers_second_file)
vector_calculator = Vector(first_vector, second_vector)
results = vector_calculator.perform_operations()
print(results)
write_data(name_output_file, results)