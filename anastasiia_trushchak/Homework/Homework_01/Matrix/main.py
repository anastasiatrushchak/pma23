import numpy as np
data1 = np.loadtxt("inputMatrix1.txt", dtype="i", delimiter=' ')
data2 = np.loadtxt("inputMatrix2.txt", dtype="i", delimiter=' ')
def sum_matrix(data1, data2):
    return [[k + n for k, n in zip(i, j)] for i, j in zip(data1, data2)]
def substruct_matrix(data1, data2):
    return [[k - n for k, n in zip(i, j)] for i, j in zip(data1, data2)]
sum_result = sum_matrix(data1, data2)
substruct_result = substruct_matrix(data1, data2)
with open("output.txt", "w") as f:
    f.write("Sum Result:\n")
    for row in sum_result:
        f.write(" ".join(map(str, row)) + "\n")

    f.write("\nSubtraction Result:\n")
    for row in substruct_result:
        f.write(" ".join(map(str, row)) + "\n")