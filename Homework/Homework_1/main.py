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


first_matrix = fill_matrix()
print(first_matrix)
while True:
    choice = int(input("1. Matrix\n2. Number"))
    if choice == 1:
        other = fill_matrix()
        print(other)
        break
    elif choice == 2:
        other = int(input("Number: "))
        break

while True:
    operator = input("+\t-\t/\t*\t-1\tend\nOperators: ")
    if operator == "end":
        break
    elif operator == '+':
        result = first_matrix + other
    elif operator == '-':
        result = first_matrix - other
    elif operator == '*':
        result = first_matrix * other
    elif operator == '/':
        result = first_matrix / other
    elif operator == "-1":
        result = first_matrix.inverse()
    print(result)





# vec = Vector.random(10)
# vec.print()
# vec.push(12)
# vec.print()
