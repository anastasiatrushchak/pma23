import numpy as np
choice = input("Matrix or Vecor? (M or V):")

if choice == 'M':
    a = int(input('size 1 matrix:'))
    matrix1 = np.random.randint(1, 11,(a,a))
    print(matrix1)
    b = int(input('size 2 matrix:'))
    matrix2 = np.random.randint(1, 11,(b,b))
    print(matrix2)
    operation = input("operation:")
    if operation == '+':
        result = matrix1+matrix2
        print(result)

    elif operation == '-':
        result = matrix1-matrix2
        print(result)

    elif operation == '*':
        result = np.dot(matrix1,matrix2)
        print(result)

    if operation == '/':

        inverse_matrix = np.linalg.inv(matrix2)
        print(inverse_matrix)
        result = np.dot(matrix1,inverse_matrix)
        print(result)
elif choice == 'V':
    a = int(input('size 1 vector:'))
    vector1 = np.random.randint(1, 11,(a))
    print(vector1)
    b = int(input('size 2 vector:'))
    vector2 = np.random.randint(1, 11,(b))
    print(vector2)
    operation = input("operation:")
    if operation == '+':
        result = vector1+vector2
        print(result)

    elif operation == '-':
        result = vector1-vector2
        print(result)

    elif operation == '*':
        result = vector1* vector2
        print(result)

    if operation == '/':
        result = vector1/vector2
        print(result)

'''size = int(input("size:"))

matrix1 = np.array([])

for i in range(size):
    element = []
    for i in range(size):
        element.append([input()])
    matrix1.append(element)
for i in matrix1:

    print(i)

size = int(input("size:"))

matrix2 = []

for i in range(size):
    element = []
    for i in range(size):
        element.append([input()])
    matrix2.append(element)
for i in matrix2:
    print(i)
'''
