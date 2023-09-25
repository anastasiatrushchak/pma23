from Vasylyshyn_Dmytro.HomeWork.Lesson_2_Matrix_Clas.Task_Vector import Vector
from typing import Final

name_input_numbers_first_file: Final[str] = 'first_vector.txt'
name_input_numbers_second_file: Final[str] = 'second_vector.txt'
name_output_file: Final[str] = 'output_vector.txt'


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


first_vector = read_data(name_input_numbers_first_file)
second_vector = read_data(name_input_numbers_second_file)

vector = Vector(first_vector, second_vector)

result_sum = vector + vector
result_subtraction = vector - vector
result_division = vector / vector
result_multiplication = vector * vector

write_data(name_output_file, [result_sum, result_subtraction, result_division, result_multiplication])
