INPUT = 'input.txt'
OUTPUT = 'output.txt'
SEPARATOR = ","

import const

with open(const.INPUT, 'r') as readFile:
    line = readFile.readline()

array = line.split(const.SEPARATOR)
array = [float(i) for i in array if i.isdigit()]
for i in range(0, 8):
    array.append(array[i] + array[i + 1])

print(array)
with open(const.OUTPUT, 'w') as writeFile:
    writeFile.write(str(array))