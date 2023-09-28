def read_vector(vector_str):
    values = vector_str.split(',')
    vector = [float(val) for val in values]
    return vector

def write_vector(vector):
    vector_str = "(" + ", ".join(map(str, vector)) + ")"
    return vector_str

def add_vectors(vector1, vector2):
    result_vector = [v1 + v2 for v1, v2 in zip(vector1, vector2)]
    return result_vector

def subtract_vectors(vector1, vector2):
    result_vector = [v1 - v2 for v1, v2 in zip(vector1, vector2)]
    return result_vector

def multiply_vectors(vector1, vector2):
    result_vector = [v1 * v2 for v1, v2 in zip(vector1, vector2)]
    return str(sum(result_vector))

try:
    with open('vector1.txt', 'r') as file:
        vector1_str = file.readline()

    with open('vector2.txt', 'r') as file:
        vector2_str = file.readline()

    vector1 = read_vector(vector1_str)
    vector2 = read_vector(vector2_str)

    result_add = add_vectors(vector1, vector2)
    result_subtract = subtract_vectors(vector1, vector2)
    result_multiply = multiply_vectors(vector1, vector2)

    with open('results.txt', 'w') as file:
        file.write("Додавання: " + write_vector(result_add) + "\n")
        file.write("Віднімання: " + write_vector(result_subtract) + "\n")
        file.write("Множення: " + result_multiply + "\n")
except Exception as e:
    print("Сталася помилка:", str(e))
