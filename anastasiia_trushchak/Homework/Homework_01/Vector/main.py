import numpy as np
data1 = np.loadtxt("vector1.txt", dtype="i", delimiter=' ')
data2 = np.loadtxt("vector2.txt", dtype="i", delimiter=' ')
def sumVect(data1, data2):
    return [i + j for i, j in zip(data1, data2)]
def substractVect(data1, data2):
    return [i - j for i, j in zip(data1, data2)]
def multiVect(data1, data2):
    return [i * j for i, j in zip(data1, data2)]
def divideVect(data1, data2):
    return [i / j for i, j in zip(data1, data2)]
sum_result = sumVect(data1,data2)
substract_result= substractVect(data1, data2)
multi_result = multiVect(data1, data2)
divide_result = divideVect(data1, data2)
with open("output.txt", "w") as f:
    f.write("Sum Result:\n")
    f.write(" ".join(map(str, sum_result)) + "\n")

    f.write("Subtraction Result:\n")
    f.write(" ".join(map(str, substract_result)) + "\n")

    f.write("Multiplication Result:\n")
    f.write(" ".join(map(str, multi_result)) + "\n")

    f.write("Division Result:\n")
    f.write(" ".join(map(str, divide_result)) + "\n")