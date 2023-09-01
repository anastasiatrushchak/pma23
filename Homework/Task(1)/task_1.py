import constants
with open(constants.INPUT, 'r') as file:
    numbers = file.readline().split()
    for i in range(len(numbers)):
        numbers[i] = int(numbers[i])
with open(constants.OUTPUT, 'w') as f:
    f.write("Result:\n ")
    f.write(str(numbers[0]) + ' ' + str(numbers[1]) + ' ')
    for i in range(0,8):
        numbers.append(numbers[-1] + numbers[-2])
        f.write(str(numbers[-1]) + ' ')
