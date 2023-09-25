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
        breakPoint = float(rf.readline())

except FileNotFoundError as e:
    print(e)

array = line.split(constants.SEPARATOR)

array = [float(i) for i in array if i.isdigit()]


class Fibonacci:

    def __init__(self, array, breakPoint):
        self.numbers = array
        self.breakPoint = breakPoint

    def addFibonacci(self, arr, i):
        result = arr
        if i == 0:
            result.append(self.numbers[i])
            result.append(self.numbers[i + 1])
            result.append(self.numbers[i] + self.numbers[i + 1])
            self.addFibonacci(result, i + 1)
        else:
            number = lambda x: x[i] + x[i + 1]
            num = number(result)
            if num < breakPoint:
                result.append(num)
                self.addFibonacci(result, i + 1)

        return result


result = Fibonacci(array, breakPoint)
breakP = result.addFibonacci([], 0)
breakP.__len__()

try:
    with open(constants.OUTPUT_FILE, 'w') as wf:
        wf.write(str(breakP))
except FileNotFoundError as e:
    print(e)
