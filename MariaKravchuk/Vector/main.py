def input_vector_file(name_file):
    vector = []
    try:
        with open(name_file, 'r') as file:
            for line in file:
                row = [int(x) for x in line.strip().split()]
                vector.append(row)
        return vector
    except FileNotFoundError:
        print(f"Error: File '{name_file}' not found.")
        return None

def result_in_file(matrix, file_name, label):
    with open(file_name, 'a') as file:
        file.write(label + ":\n")
        for row in matrix:
            file.write(' '.join(map(str, row)) + '\n')
        file.write('\n')

def multiply_vectors(first_vector, second_vector):
    if len(first_vector) != len(second_vector) or len(first_vector[0]) != len(second_vector[0]):
        return None
    result = []
    for i in range(len(first_vector)):
        row = []
        for j in range(len(first_vector[0])):
            row.append(first_vector[i][j] * second_vector[i][j])
        result.append(row)
    return result

def add_vectors(first_vector, second_vector):
    if len(first_vector) != len(second_vector) or len(first_vector[0]) != len(second_vector[0]):
        return None
    result = []
    for i in range(len(first_vector)):
        row = []
        for j in range(len(first_vector[0])):
            row.append(first_vector[i][j] + second_vector[i][j])
        result.append(row)
    return result

def sub_vectors(first_vector, second_vector):
    if len(first_vector) != len(second_vector) or len(first_vector[0]) != len(second_vector[0]):
        return None
    result = []
    for i in range(len(first_vector)):
        row = []
        for j in range(len(first_vector[0])):
            row.append(first_vector[i][j] - second_vector[i][j])
        result.append(row)
    return result

def divide_vectors(first_vector, second_vector):
    if len(first_vector) != len(second_vector) or len(first_vector[0]) != len(second_vector[0]):
        return None
    result = []
    for i in range(len(first_vector)):
        row = []
        for j in range(len(first_vector[0])):
            try:
                result_value = first_vector[i][j] / second_vector[i][j]
            except ZeroDivisionError:
                print("Error: Division by zero encountered.")
                return None  
            row.append(result_value)
        result.append(row)
    return result


first_vector = input_vector_file('first_vector.txt')
second_vector = input_vector_file('second_vector.txt')

with open("output.txt", 'w') as file:
    file.write("")

result_in_file(first_vector, "output.txt", "Vector 1")
result_in_file(second_vector, "output.txt", "Vector 2")

result_vector = multiply_vectors(first_vector, second_vector)
if result_vector is not None:
    result_in_file(result_vector, "output.txt", "Multiplication")
else:
    print("Multiplication is not possible.")

add_vector = add_vectors(first_vector, second_vector)
if add_vector is not None:
    result_in_file(add_vector, "output.txt", "Addition")
else:
    print("Addition is not possible.")


sub_vector = sub_vectors(first_vector, second_vector)
if sub_vector is not None:
    result_in_file(sub_vector, "output.txt", "Subtraction")
else:
    print("Subtraction is not possible.")


div_vector = divide_vectors(first_vector, second_vector)
if div_vector is not None:
    result_in_file(div_vector, "output.txt", "Division")
else:
    print("Division is not possible.")
