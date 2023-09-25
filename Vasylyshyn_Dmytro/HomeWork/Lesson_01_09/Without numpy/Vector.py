with open('FirstVector.txt', 'r') as data:
    firstVector = data.readline().split()

with open('SecondVector.txt', 'r') as data:
    secondVector = data.readline().split()

firstVector = [int(num) for num in firstVector]
secondVector = [int(num) for num in secondVector]

vectorSumm = []
vectorSubtract = []
vectorMultiplication = []
vectorDivision = []

vectorSumm = [x + y for x, y in zip(firstVector, secondVector)]
vectorSubtract = [x - y for x, y in zip(firstVector, secondVector)]
vectorMultiplication = [x * y for x, y in zip(firstVector, secondVector)]
vectorDivision = [x / y for x, y in zip(firstVector, secondVector)]


with open('OutputVector.txt', 'w') as file:
    file.write("Vector Sum: ")
    #    file.write(str (vectorSumm))
    file.write("first vector + second vector\n")
    for row in range(len(vectorSumm)):
        file.write(str(firstVector[row]) + ' ')

    file.write(' + ')

    for row in range(len(vectorSumm)):
        file.write(str(secondVector[row]) + ' ')

    file.write("\n")

    for row in range(len(vectorSumm)):
        file.write(str(vectorSumm[row]) + ' ')

    file.write("\n")

    file.write("Vector Subtract:\n")
    #   file.write(str (vectorSubtract))
    for row in range(len(vectorSubtract)):
        file.write(str(vectorSubtract[row])+' ')

    file.write("\n")

    file.write("Vector Multiplication:\n")
    file.write(str (vectorMultiplication))

    file.write("\n")

    file.write("Vector Division:\n")
    file.write(str (vectorDivision))

