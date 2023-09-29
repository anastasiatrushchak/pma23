import numpy as np

with open("input_vectors.txt", "r") as readFile:
    firstVector = np.array(readFile.readline().strip().split(','), dtype=float)
    secondVector = np.array(readFile.readline().strip().split(','), dtype=float)

print(firstVector, secondVector)
# summ = np.add(firstVector, secondVector)
# substr = np.subtract(firstVector, secondVector)
# multiplication = np.multiply(firstVector, secondVector)
# division = np.divide(firstVector, secondVector)
summ = []
for i in range(0, len(firstVector)):
    summ.append(firstVector[i] + secondVector[i])
substr = []
for i in range(0, len(firstVector)):
    substr.append(firstVector[i] - secondVector[i])
multiplication = []
for i in range(0, len(firstVector)):
    multiplication.append(firstVector[i] * secondVector[i])
division = []
for i in range(0, len(firstVector)):
    try:
        division.append(firstVector[i] / secondVector[i])
    except ZeroDivisionError:
        print("Неможливо поділити на нуль")
        division.append(0)

output_string = f"Сума: {summ}\nРізниця: {substr}\nДобуток: {multiplication}\nЧастка: {division}\n"

print(output_string)

with open("output_vector.txt", "w") as writeFile:
    writeFile.write(output_string)
