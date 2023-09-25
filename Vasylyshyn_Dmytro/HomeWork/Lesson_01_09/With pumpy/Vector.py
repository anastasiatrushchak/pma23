import numpy as np

with open('FirstVector.txt', 'r') as data:
    firstVector = data.readline().split()

with open('SecondVector.txt', 'r') as data:
    secondVector = (data.readline().split())

firstVector = np.array(firstVector,int)
secondVector = np.array(secondVector,int)

vectorSumm = firstVector + secondVector
vectorSubtract = firstVector - secondVector
vectorMultiplication = firstVector * secondVector
vectorDivision = firstVector / secondVector

with open('VectorOutput.txt', 'w') as file:
    file.write("Vector Summ:\n")
    file.write(str(vectorMultiplication))

    file.write("\n")

    file.write("Vector Subtract:\n")
    file.write(str(vectorSubtract))

    file.write('\n')

    file.write("Vector Multiplication:\n")
    file.write(str(vectorMultiplication))

    file.write("\n")

    file.write("Vector Division:\n")
    file.write(str(vectorDivision))