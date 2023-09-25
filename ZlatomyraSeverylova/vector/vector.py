INPUT = 'input_vector.txt'
OUT = 'out_vector.txt'
ZERO_DIVISION_ERROR = 'division by zero'
FILE_NOT_FOUND_ERROR = 'No such file or directory'
try:
    with open(INPUT, 'r') as f:
        vector_a = [int(num) for num in f.readline().split()]
        vector_b = [int(num) for num in f.readline().split()]
except FileNotFoundError:
    print(FILE_NOT_FOUND_ERROR)
    exit(-1)


def vector_sum(vector_a, vector_b):
    result = []
    for i in range(len(vector_a)):
        result.append(vector_a[i] + vector_b[i])
    return result


def vector_difference(vector_a, vector_b):
    result = []
    for i in range(len(vector_a)):
        result.append(vector_a[i] - vector_b[i])
    return result


def vector_mult(vector_a, vector_b):
    result = []
    for i in range(len(vector_a)):
        result.append(vector_a[i] * vector_b[i])
    return result


def vector_div(vector_a, vector_b):
    result = []
    for i in range(len(vector_a)):
        try:
            result.append(vector_a[i] / vector_b[i])
        except ZeroDivisionError:
            print(ZERO_DIVISION_ERROR)
            exit(-1)
    return result


try:
    with open(OUT, 'w') as f:
        f.write("Sum of vector: ")
        f.write(str(vector_sum(vector_a, vector_b)))
        f.write("\n")
        f.write("Difference of vector: ")
        f.write(str(vector_difference(vector_a, vector_b)))
        f.write("\n")
        f.write("Multiplication of vectors: ")
        f.write(str(vector_mult(vector_a, vector_b)))
        f.write("\n")
        f.write("Division of vectors: ")
        f.write(str(vector_div(vector_a, vector_b)))
except FileNotFoundError:
    print(FILE_NOT_FOUND_ERROR)
    exit(-1)
