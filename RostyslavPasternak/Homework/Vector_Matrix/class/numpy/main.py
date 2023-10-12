from Matrix import Matrix
from Vector import Vector
import numpy as np
def fill_matrix():
    while True:
        choice = int(input("Fill in the matrix\n\t1. Random\n\t2. From file\n\t3. From the keyboard\n "))
        if choice == 1:
            row = int(input("Input row: "))
            column = int(input("Input column: "))
            return Matrix.random(row, column)
        elif choice == 2:
            file_name = input("File name: ")
            return Matrix.from_file(file_name)
        elif choice == 3:
            row = int(input("Input row: "))
            column = int(input("Input column: "))

            matrix_np = np.empty((row, column), dtype=int)

            for i in range(row):
                for j in range(column):
                    matrix_np[i][j] = int(input(f"Element [{i + 1}][{j + 1}]: "))
            return Matrix(matrix_np)
        else:
            print("Invalid choice. Please select 1, 2, or 3.")

def task_matrix():
    matrix = fill_matrix()
    print(matrix)
    while True:
        choice = int(input("Second element\n\t1. Vector\n\t2. Number\n"))
        if choice == 1:
            other = fill_matrix()
            break
        if choice == 2:
            other = int(input("Number: "))
            break

    while True:
        result = None
        operator = int(input("1. Add\n2. Subtraction\n3. Multiplication\n4. Division\n5. Inverse\n0. Cancel\n"))
        if operator == 1:
            result = matrix + other
        elif operator == 2:
            result = matrix - other
        elif operator == 3:
            result = matrix * other
        elif operator == 4:
            result = matrix / other
        elif operator == 5:
            result = matrix.inverse()
        else:
            break
        print(result)
        result.str_to_file()

def fill_vector():
    while True:
        choice = int(input("How to fill a vector\n\t1. From file\n\t2. From random\n\t3. From the keyboard\n\t0. Cancel\n"))
        if choice == 1:
            fileName = input("File name: ")
            return Vector.from_file(fileName)
        elif choice == 2:
            size = int(input("Size: "))
            return Vector.random(size)
        elif choice == 3:
            size = int(input("Input size: "))

            vector_np = np.empty((size), dtype=int)

            for i in range(size):
                vector_np[i] = int(input(f"Element [{i + 1}]: "))
            return Vector(vector_np)
        else:
            break

def task_vector():
    vector = fill_vector()
    print(vector)
    while True:
        choice = int(input("Second element\n\t1. Vector\n\t2. Number\n"))
        if choice == 1:
            other = fill_vector()
            break
        if choice == 2:
            other = int(input("Number: "))
            break

    while True:
        result = None
        operator = int(input("1. add\n2. subtraction\n3. multiplication\n4. division\n0. Cancel\n"))
        if operator == 1:
            result = vector + other
        elif operator == 2:
            result = vector - other
        elif operator == 3:
            result = vector * other
        elif operator == 4:
            result = vector / other
        else:
            break
        print(result)
        result.str_to_file()

while True:
    choice = int(input("1. Matrix\n2. Vector\n0. Cancel \n"))
    if choice == 1:
        task_matrix()
    elif choice == 2:
        task_vector()
    else:
        break
