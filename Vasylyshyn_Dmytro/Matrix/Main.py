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

matrixSumm = [[0 for _ in range(len(firstMatrix[0]))] for _ in range(len(firstMatrix))]
matrixSubtract = [[0 for _ in range(len(firstMatrix[0]))] for _ in range(len(firstMatrix))]
matrixMultiplication = [[0 for _ in range(len(firstMatrix[0]))] for _ in range(len(firstMatrix))]
reversMatrix = [[0 for _ in range(len(firstMatrix[0]))] for _ in range(len(firstMatrix))]
matrixDivision = [[0 for _ in range(len(firstMatrix[0]))] for _ in range(len(firstMatrix))]

for row in range(len(firstMatrix)):
    rowList = []
    for column in range(len(firstMatrix[0])):
        firstMatrix[row][column] = int(firstMatrix[row][column])
        secondMatrix[row][column] = int(secondMatrix[row][column])
        matrixSumm[row][column] = firstMatrix[row][column] + secondMatrix[row][column]
        matrixSubtract[row][column] = firstMatrix[row][column] - secondMatrix[row][column]

for i in range(len(secondMatrix)):
    row = []
    for j in range(len(secondMatrix[0])):
        row.append(secondMatrix[j][i])
    reversMatrix[i] = (row)

for i in range(len(firstMatrix)):
    for j in range(len(secondMatrix[0])):
        for k in range(len(secondMatrix)):
            matrixMultiplication[i][j] += firstMatrix[i][k] * secondMatrix[k][j]
            matrixDivision[i][j] += firstMatrix[i][k] * reversMatrix[k][j]

with open('OutputMatrix.txt', 'w') as file:
    file.write("Matrix Sum:\n")
    #    file.write(str (matrixSumm))
    for row in range(len(matrixSumm)):
        file.write(str(matrixSumm[row]) + '\n')

    file.write("Matrix Subtract:\n")
    #   file.write(str (matrixSubtract))
    for row in range(len(matrixSubtract)):
        file.write(str(matrixSubtract[row]) + '\n')

    file.write("Matrix Multiplication:\n")
    #   file.write(str (matrixMultiplication))
    for row in range(len(matrixMultiplication)):
        file.write(str(matrixMultiplication[row]) + '\n')

    file.write("Matrix Division:\n")
    #   file.write(str (matrixDivision))
    for row in range(len(matrixDivision)):
        file.write(str(matrixDivision[row]) + '\n')
