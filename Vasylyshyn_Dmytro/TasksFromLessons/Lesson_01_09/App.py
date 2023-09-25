from typing import Final
nameInputFile:Final[str]='file.txt'
nameOutputFile:Final[str]='output.txt'

with open(nameInputFile, 'r') as data:
    numbers = data.readline().split()

numbers = [int(num) for num in numbers]

while len(numbers) < 10:
    nextNum = numbers[-1] + numbers[-2]
    numbers.append(nextNum)

with open(nameOutputFile, 'w') as file:
    file.write(str(numbers))

print(
f"""
file with input data is named: {nameInputFile}
file with output data which contains result: {nameOutputFile}
""")

