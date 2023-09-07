import numpy as np
firstMatrix = []
secondMatrix = []

with open("matrices_input.txt", "r") as readFile:
    temp = firstMatrix

    for line in readFile:
        line = line.strip()
        if not line:
            temp = secondMatrix
            continue
        row = [float(i) for i in line.split(" ")]
        temp.append(row)

firstMatrix = np.matrix(firstMatrix)
secondMatrix = np.matrix(secondMatrix)
print(firstMatrix, "\n\n", secondMatrix)

summ = np.add(firstMatrix, secondMatrix)
substr = np.subtract(firstMatrix, secondMatrix)
multiplication = np.dot(firstMatrix, secondMatrix)
division = np.dot(firstMatrix, np.linalg.inv(secondMatrix))
output_string = f"Сума:\n {summ}\nРізниця:\n {substr}\nДобуток:\n {multiplication}\nЧастка:\n {division}\n"

with open("output_matrix.txt", "w") as writeFile:
    writeFile.write(output_string)
