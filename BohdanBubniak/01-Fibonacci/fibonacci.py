with open('input.txt', 'r') as file:
    data = file.readline().split(',')
    num1 = int(data[0].strip())
    num2 = int(data[1].strip())

with open('steps.txt', 'r') as file:
    steps = int(file.readline().strip())

result = [num1, num2]

for _ in range(2, steps):  
    next_num = result[-1] + result[-2]
    result.append(next_num)

with open('output.txt', 'w') as file:
    file.write(','.join(map(str, result)))
