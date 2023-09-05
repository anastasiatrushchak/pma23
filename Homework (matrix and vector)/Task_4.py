import numpy as np
def print_matrix(matrix):
    for i in matrix:
        print(i)
class Matrix:

   def __init__(self,matrix):
       self.matrix=matrix
   def __eq__(self, other):
       return len(self.matrix)==len(other.matrix)
   def __len__(self):
       return len(self.matrix)
   def __add__(self, matrix_other):
       matrix_rez=[]
       if len(self.matrix) == len(matrix_other.matrix) and len(self.matrix[0]) == len(matrix_other.matrix[0]):
           for i in range(len(matrix_other)):
               row_matrix_rez = []
               for j in range(len(matrix_other.matrix[0])):
                   row_matrix_rez.append(float(self.matrix[i][j]) + float(matrix_other.matrix[i][j]))
               matrix_rez.append(row_matrix_rez)
           return matrix_rez
       else:
           return "Не можливо додати матриці"
   def __sub__(self, matrix_other):
       if len(self.matrix) == len(matrix_other.matrix) and len(self.matrix[0]) == len(matrix_other.matrix[0]):
           matrix_rez = []
           for i in range(len(matrix_other.matrix)):
               row_matrix_rez = []
               for j in range(len(matrix_other.matrix[0])):
                   row_matrix_rez.append(float(self.matrix[i][j]) - float(matrix_other.matrix[i][j]))
               matrix_rez.append(row_matrix_rez)
           return matrix_rez
       else:
           return "Не можливо відняти матриці"
   def __mul__(self, matrix_other):
       if len(self.matrix[0]) == len(matrix_other.matrix):
           matrix_rez=[]
           for i in range(len(self.matrix)):
               row = []
               for j in range(len(matrix_other.matrix[0])):
                   number = 0
                   for k in range(len(self.matrix[0])):
                       number += int(self.matrix[i][k]) * int(matrix_other.matrix[k][j])
                   row.append(number)
               matrix_rez.append(row)
           return matrix_rez
       else:
           return "Не можливо помножити"
   def __truediv__(self, matrix_other):
       try:
           inverse_matrix2 = np.linalg.inv(matrix_other.matrix)
           return self* Matrix(inverse_matrix2)
       except:
           return "Не можливо поділити матрциі"
file1=[]
file2=[]


with open("matrix1.txt", "r") as lines:
    lines = lines.readlines()

    for line in lines:
        row = [float(x) for x in line.split()]
        file1.append(row)

with open("matrix2.txt", "r") as lines:
    lines = lines.readlines()

    for line in lines:
        row = [float(x) for x in line.split()]
        file2.append(row)
matrix1=Matrix(file1)
matrix2=Matrix(file2)

rez=matrix1+matrix2
print("Додавання")
print_matrix(rez)

rez=matrix1-matrix2
print("Віднімання")
print_matrix(rez)

rez=matrix1*matrix2
print("Множення")
print_matrix(rez)

rez=matrix1/matrix2
print("Ділення")
print(rez)

