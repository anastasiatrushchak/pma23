import os

def file_exists(filename):
    return os.path.isfile(filename)

def read_matrix(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
    matrix = []
    for line in lines:
        rows = [int(x) for x in line.split()]
        matrix.append(rows)
    return matrix

def write_matrix(matrix, filename):
    with open(filename, 'a') as file:
        file.write("matrix result:\n")
        for rows in matrix:
            file.write(' '.join(map(str, rows)) + '\n')

first_matrix = read_matrix('first_input.txt')
second_matrix = read_matrix('second_input.txt')

#файли не існують
try:
    with open('first_input.txt', 'r') as file:
        data = file.read()
except FileNotFoundError:
    print("file doesnt exist.")

    try:
        with open('second_input.txt', 'r') as file:
            data = file.read()
    except FileNotFoundError:
        print("file is not found.")

#файли пусті
try:
    with open('first_input.txt', 'r') as file:
        data = file.read()
    if not data:
        print("file is empty")
except FileNotFoundError:
    print("file not found.")

try:
    with open('second_input.txt', 'r') as file:
        data = file.read()
    if not data:
        print("file is empty")
except FileNotFoundError:
    print("file not found.")

if len(first_matrix) != len(second_matrix) or len(first_matrix[0]) != len(second_matrix[0]):
    print("the sizes doesnt match.")
else:
    result_addition = []
    result_subtraction = []

    for i in range(len(first_matrix)):
        add_rows = []
        sub_rows = []
        for j in range(len(first_matrix[0])):
            add_rows.append(first_matrix[i][j] + second_matrix[i][j])
            sub_rows.append(first_matrix[i][j] - second_matrix[i][j])
        result_addition.append(add_rows)
        result_subtraction.append(sub_rows)

    write_matrix(result_subtraction, 'output_subtraction.txt')
    write_matrix(result_addition, 'output_addition.txt')

    print("Addition result:")
    for rows in result_addition:
      print(rows)

    print("Subtraction result:")
    for rows in result_subtraction:
      print(rows)
