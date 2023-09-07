import numpy as np


def read_vectors(filename):
    try:
        with open(filename, 'r') as f:
            vectorA = np.array([float(num) for num in f.readline().split(',')])
            vectorB = np.array([float(num) for num in f.readline().split(',')])
        return vectorA, vectorB
    except Exception as e:
        print(f"Error reading vectors from file: {e}")
        return None, None


def write_vector(filename, vector):
    try:
        with open(filename, 'w') as f:
            f.write(', '.join(['{:0.5g}'.format(x) for x in vector]) + '\n')
    except Exception as e:
        print(f"Error writing vector to file: {e}")


def vector_add(A, B):
    return A + B


def vector_subtract(A, B):
    return A - B


def vector_multiply(A, B):
    return A * B


def vector_divide(A, B):
    try:
        return A / B
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
        return None


VectorA, VectorB = read_vectors('vectors.txt')
if VectorA is None or VectorB is None:
    print("Exiting due to error.")
else:
    operation = input("Enter operation (add, subtract, multiply, divide): ")
    if operation == 'add':
        result = vector_add(VectorA, VectorB)
    elif operation == 'subtract':
        result = vector_subtract(VectorA, VectorB)
    elif operation == 'multiply':
        result = vector_multiply(VectorA, VectorB)
    elif operation == 'divide':
        result = vector_divide(VectorA, VectorB)
        if result is None:
            print("Exiting due to error.")
    else:
        print("Invalid operation")

    if result is not None:
        print(', '.join('{:0.5g}'.format(x) for x in result))
        write_vector('result_vector.txt', result)
