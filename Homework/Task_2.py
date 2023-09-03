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

if len(matrix1)==len(matrix2) and len(matrix1[0])==len(matrix2[0]):
    for i in range(len(matrix2)):
        row_matrix_rez=[]
        for j in range(len(matrix2[0])):
            row_matrix_rez.append(float(matrix1[i][j]) + float(matrix2[i][j]))
        matrix_rez.append(row_matrix_rez)

    print("Додавання: ")
    print_matrix(matrix_rez)

    matrix_rez=[]
    for i in range(len(matrix2)):
        row_matrix_rez=[]
        for j in range(len(matrix2[0])):
            row_matrix_rez.append(int(matrix1[i][j])-int(matrix2[i][j]))
        matrix_rez.append(row_matrix_rez)
    print("Віднімання: ")
    print_matrix(matrix_rez)
    matrix_rez=[]
else:
    print("Не можливо додати і відняти ці матриці")
if len(matrix1[0])==len(matrix2):

    for i in range(len(matrix1)):
        row=[]
        for j in range(len(matrix2[0])):
            number=0
            for k in range(len (matrix1[0])):
                number += int(matrix1[i][k]) * int(matrix2[k][j])
            row.append(number)
        matrix_rez.append(row)
    print("Множення:")
    print_matrix(matrix_rez)
else:
    print("Не можливо помножити")
try:
    inverse_matrix2=np.linalg.inv(matrix2)

    if len(matrix1[0])==len(inverse_matrix2):

        for i in range(len(matrix1)):
            row=[]
            for j in range(len(inverse_matrix2[0])):
                number=0
                for k in range(len (matrix1[0])):
                    number += int(matrix1[i][k]) * int(inverse_matrix2[k][j])
                row.append(number)
            matrix_rez.append(row)
        print("Ділення:")
        print_matrix(matrix_rez)
except:
    print("Не можливо поділити матриці")
