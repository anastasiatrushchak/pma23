# Practical - 15.09.2023
import os

import constants


class FileIsEmpty(Exception):

    def __init__(self, message="File is empty!"):
        self.message = message
        super().__init__(self.message)


try:
    with open(constants.INPUT_FILE, 'r') as rf:
        if os.path.getsize(constants.INPUT_FILE) == 0:
            raise FileIsEmpty
        line = rf.readline()

    with open(constants.PARAMETERS_FILE, 'r') as rf:
        breakPoint = rf.readline()

except FileNotFoundError as e:
    print(e)

breakPoint = float(breakPoint)

array = line.split(constants.SEPARATOR)

line = [float(i) for i in line if i.isdigit()]

for i in range(len(array)):
    array[i] = float(array[i])


def addFibonacci(i):
    num = array[i] + array[i + 1]
    if num < breakPoint:
        array.append(num)
        addFibonacci(i + 1)


addFibonacci(0)

try:
    with open(constants.OUTPUT_FILE, 'w') as wf:
        wf.write(str(array))
except FileNotFoundError as e:
    print(e)
