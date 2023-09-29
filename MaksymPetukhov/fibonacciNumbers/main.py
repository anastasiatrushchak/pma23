# Practical - 01.09.2023

import constants

with open(constants.INPUT_FILE, 'r') as rf:
    line = rf.readline()

array = line.split(constants.SEPARATOR)

line = [float(i) for i in line if i.isdigit()]

for i in range(0, 10):
    array.append(array[i] + array[i + 1])

with open(constants.OUTPUT_FILE, 'w') as wf:
    wf.write(str(array))