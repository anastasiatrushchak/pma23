import numpy as np

firstMatrix = []
secondMatrix = []

with open('FirstMatrix.txt', 'r') as firstFileMatrix:
    for line in firstFileMatrix:
        row = [int(x) for x in line.split()]
        firstMatrix.append(row)

with open('SecondMatrix.txt', 'r') as secondFileMatrix:
    for line in secondFileMatrix:
        row = [int(x) for x in line.split()]
        secondMatrix.append(row)

firstMatrix=np.array(firstMatrix)
secondMatrix=np.array(secondMatrix)

matrixSumm = firstMatrix+secondMatrix
matrixSubtract = firstMatrix-secondMatrix
matrixMultiplication = np.dot(firstMatrix,secondMatrix)
matrixDivision=np.dot(firstMatrix,np.transpose(secondMatrix))

with open('MatrixOutput.txt', 'w') as file:
    file.write("Matrix Sum:\n")
    file.write(str (matrixSumm)+'\n')

    file.write("Matrix Subtract:\n")
    file.write(str (matrixSubtract)+'\n')

    file.write("Matrix Multiplication:\n")
    file.write(str (matrixMultiplication)+'\n')

    file.write("Matrix Division:\n")
    file.write(str (matrixDivision)+'\n')





