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

matrix1=np.matrix(matrix1)
matrix2=np.matrix(matrix2)
try:
    matrix_rez=matrix1+matrix2

    print("Додавання: ")
    print_matrix(matrix_rez)

    matrix_rez=matrix1-matrix2
    print("Віднімання: ")
    print_matrix(matrix_rez)

except:
    print("Не можливо додати і відняти ці матриці")
try:
    matrix_rez=matrix1*matrix2
    print("Множення:")
    print_matrix(matrix_rez)
except:
    print("Не можливо помножити")
try:
        matrix_rez=matrix1/matrix2
        print("Ділення:")
        print_matrix(matrix_rez)
except:
    print("Не можливо поділити матриці")
