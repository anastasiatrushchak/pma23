import numpy as np

choice = input("Matrix or Vecor? (M or V):")

if choice == 'M':

    matrix1 = np.loadtxt('inputm1.txt')
    print("Matrix 1\n",matrix1)
    matrix2 = np.loadtxt('inputm2.txt')
    print("Matrix 2\n",matrix2)
    operation = input("operation:")

    if operation == '+':
        result = matrix1 + matrix2
        print("result:\n",result)
        with open('outputm.txt', 'w') as file:
            file.write("Matrix Sum:\n")
            for row in range(len(result)):
                file.write(str(result[row]) + '\n')
    elif operation == '-':
        result = matrix1-matrix2
        print("result:\n",result)
        with open('outputm.txt', 'w') as file:
            file.write("Matrix Sub:\n")
            for row in range(len(result)):
                file.write(str(result[row]) + '\n')

    elif operation == '*':
        result = np.dot(matrix1,matrix2)
        print("result:\n",result)
        with open('outputm.txt', 'w') as file:
            file.write("Matrix mult:\n")
            for row in range(len(result)):
                file.write(str(result[row]) + '\n')

    elif operation == '/':
        try:
            inverse_matrix = np.linalg.inv(matrix2)
            print("inverse matrix: \n",inverse_matrix,"\n")
            result = np.dot(matrix1,inverse_matrix)
            print( "result:\n",result)
            with open('outputm.txt', 'w') as file:
                file.write("Matrix division:\n")
                for row in range(len(result)):
                    file.write(str(result[row]) + '\n')
        except Exception as e:
            print("Помилка: ", e)
elif choice == 'V':
    vector1 = np.loadtxt('inputv1.txt')
    print(vector1)
    vector2 = np.loadtxt('inputv2.txt')
    print(vector2)
    operation = input("operation:")
    if operation == '+':
        result = vector1+vector2
        print(result)
        with open('outputm.txt', 'w') as file:
            file.write("Vector sum:\n")
            file.write(str(result) + '\n')

    elif operation == '-':
        result = vector1-vector2
        print("result:\n",result)
        with open('outputm.txt', 'w') as file:
            file.write("Vector sub:\n")
            file.write(str(result) + '\n')

    elif operation == '*':
        result = vector1 * vector2
        print("result:\n",result)
        with open('outputm.txt', 'w') as file:
            file.write("Vector mult:\n")
            file.write(str(result) + '\n')

    elif operation == '/':
        result = vector1 / vector2
        print("result:\n", result)
        with open('outputm.txt', 'w') as file:
            file.write("Vector division:\n")
            file.write(str(result) + '\n')


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
