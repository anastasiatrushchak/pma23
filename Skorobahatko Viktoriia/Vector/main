def read_vectors(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        vector1 = tuple(map(float, lines[0].strip().split(',')))
        vector2 = tuple(map(float, lines[1].strip().split(',')))
        return vector1, vector2

def write_vector(filename, vector, operation=None):
    with open(filename, 'a') as file:
        if operation:
            file.write(f"{vector} {operation}\n")
        else:
            file.write(','.join(map(str, vector)) + '\n')

def add_vectors(vec1, vec2):
    result = tuple(x + y for x, y in zip(vec1, vec2))
    return result

def subtract_vectors(vec1, vec2):
    result = tuple(x - y for x, y in zip(vec1, vec2))
    return result

def multiply_vectors(vec1, vec2):
    result = tuple(x * y for x, y in zip(vec1, vec2))
    return result

def divide_vectors(vec1, vec2):
    result = tuple(x / y for x, y in zip(vec1, vec2))
    return result

def main():
    input_file = 'input.txt'
    output_file = 'output.txt'

    vector1, vector2 = read_vectors(input_file)

    with open(output_file, 'w') as file:
        result = add_vectors(vector1, vector2)
        write_vector(output_file, result, '+')

        result = subtract_vectors(vector1, vector2)
        write_vector(output_file, result, '-')

        result = multiply_vectors(vector1, vector2)
        write_vector(output_file, result, '*')

        result = divide_vectors(vector1, vector2)
        write_vector(output_file, result, '/')


