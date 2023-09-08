import numpy as np
def print_matrix(matrix):
    for i in matrix:
        print(i)

matrix1=[]
matrix2=[]
matrix_rez = []

with open("matrix1.txt", "r") as lines:
    lines = lines.readlines()

    for line in lines:
        row = [float(x) for x in line.split()]
        matrix1.append(row)

with open("matrix2.txt", "r") as lines:
    lines = lines.readlines()

    for line in lines:
        row = [float(x) for x in line.split()]
        matrix2.append(row)

try:
    matrix_sum=[]
    for i in range(max(len(matrix2), len(matrix1))):
        row_matrix_rez=[]
        for j in range(max(len(matrix2[0]), len(matrix1[0]))):
            row_matrix_rez.append(float(matrix1[i][j]) + float(matrix2[i][j]))
        matrix_sum.append(row_matrix_rez)



    matrix_divide=[]
    for i in range(len(matrix2)):
        row_matrix_rez=[]
        for j in range(len(matrix2[0])):
            row_matrix_rez.append(int(matrix1[i][j])-int(matrix2[i][j]))
        matrix_divide.append(row_matrix_rez)

    with open("matrix_rez.txt", 'w') as file:
        file.write("Додавання:\n")
        for i in matrix_sum:
            file.write(str(i)+'\n')

        file.write("Віднімання:\n")
        for i in matrix_divide:
            file.write(str(i)+'\n')

except:
    with open("matrix_rez.txt", 'w') as file:
        file.write("Не можливо додати і відняти ці матриці\n")

try:

    for i in range(len(matrix1)):
        row=[]
        for j in range(len(matrix2[0])):
            number=0
            for k in range(max(len(matrix1[0]), len(matrix2))):
                number += int(matrix1[i][k]) * int(matrix2[k][j])
            row.append(number)
        matrix_rez.append(row)

    with open("matrix_rez.txt", 'a') as file:
        file.write("Множення:\n")
        for i in matrix_rez:
            file.write(str(i)+'\n')
except:
    with open("matrix_rez.txt", 'a') as file:
        file.write("Не можливо помножити\n")

try:
    matrix_rez=[]
    inverse = []

    n=len(matrix2)
    for i in range(n):
        row = []
        for j in range(n):
            if i == j:
                row.append(1)
            else:
                row.append(0)
        inverse.append(row)

    for col in range(n):
        # Знаходимо головний елемент у поточному стовпці
        max_val = abs(matrix2[col][col])
        max_row = col
        for k in range(col + 1, n):
            if abs(matrix2[k][col]) > max_val:
                max_val = abs(matrix2[k][col])
                max_row = k

        # Обмінюємо рядки так, щоб головний елемент був на діагоналі
        matrix2[col], matrix2[max_row] = matrix2[max_row], matrix2[col]
        inverse[col], inverse[max_row] = inverse[max_row], inverse[col]

        # Ділимо головний рядок на головний елемент, щоб зробити його 1
        pivot = matrix2[col][col]
        for j in range(n):
            matrix2[col][j] /= pivot
            inverse[col][j] /= pivot

        # Віднімаємо інші рядки, щоб зробити інші елементи в стовпці нульовими
        for i in range(n):
            if i != col:
                factor = matrix2[i][col]
                for j in range(n):
                    matrix2[i][j] -= factor * matrix2[col][j]
                    inverse[i][j] -= factor * inverse[col][j]





    for i in range(len(matrix1)):
        row=[]
        for j in range(len(inverse[0])):
            number=0
            for k in range(max(len(matrix1[0]), len(inverse))):
                number += float(matrix1[i][k]) * float(inverse[k][j])
            row.append(number)
        matrix_rez.append(row)

    with open("matrix_rez.txt", 'a') as file:
        file.write("Ділення:\n")
        for i in matrix_rez:
            file.write(str(i)+'\n')
except:
    with open("matrix_rez.txt", 'a') as file:
        file.write("Не можливо поділити матриці\n")

