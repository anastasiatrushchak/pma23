def read_vectors_from_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        first_vector = [float(x) for x in lines[0].split()]
        second_vector = [float(x) for x in lines[1].split()]
    return first_vector, second_vector

#додавання
def add_vectors(first_vector, second_vector):
    return [x + y for x, y in zip(first_vector, second_vector)]

#віднімання
def subtract_vectors(first_vector, second_vector):
    return [x - y for x, y in zip(first_vector, second_vector)]

#множення
def multiply_vectors(first_vector, second_vector):
    return [x * y for x, y in zip(first_vector, second_vector)]

#ділення
def divide_vectors(first_vector, second_vector):
    return [x / y for x, y in zip(first_vector, second_vector)]

input_filename = 'input.txt'
output_filename = 'output.txt'
first_vector, second_vector = read_vectors_from_file(input_filename)

result_add = add_vectors(first_vector, second_vector)
result_subtract = subtract_vectors(first_vector, second_vector)
result_multiply = multiply_vectors(first_vector, second_vector)
result_divide = divide_vectors(first_vector, second_vector)

with open(output_filename, 'w') as file:
    file.write("add: {}\n".format(result_add))
    file.write("subtract: {}\n".format(result_subtract))
    file.write("multiply: {}\n".format(result_multiply))
    file.write("divide: {}\n".format(result_divide))
