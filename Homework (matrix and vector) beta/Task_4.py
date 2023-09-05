import numpy as np
class Matrix:

   def __init__(self,matrix):
       self.matrix=np.matrix(matrix)
   def __len__(self):
       return len(self.matrix)
   def __add__(self, matrix_other):

       try:
           matrix_rez = self.matrix*matrix_other.matrix
           return matrix_rez
       except:
           return "Неможливо додати матриці"
   def __sub__(self, matrix_other):
       try:
           matrix_rez=self.matrix-matrix_other.matrix
           return matrix_rez
       except:
           return "Неможливо відняти матриці"
   def __mul__(self, matrix_other):
       try:
           matrix_rez=self.matrix*matrix_other.matrix
           return matrix_rez
       except:
           return "Неможливо помножити  матриці"
   def __truediv__(self, matrix_other):
       try:
           matrix_rez=self.matrix/matrix_other.matrix
           return matrix_rez
       except:
           return "Неможливо поділити матрциі"


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
matrix1 = Matrix(file1)
matrix2 = Matrix(file2)


print("Додавання")
print(matrix1+matrix2)


print("Віднімання")
print(matrix1-matrix2)


print("Множення")
print(matrix1*matrix2)


print("Ділення")
print(matrix1/matrix2)

