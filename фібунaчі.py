try:
    with open('input.txt', 'r') as input_file:
        fibonacci = list( map(int, input_file.readline().split()))
        if not fibonacci:
            print("the file is empty")
except FileNotFoundError:
    print("file not found")

try:
    with open('steps.txt', 'r') as steps_file:
        steps = int(steps_file.readline())
        if not steps:
            print("the file is empty")
except FileNotFoundError:
    print("file not found")

for i in range(steps - 2):
        next_number = fibonacci[-1] + fibonacci[-2]
        fibonacci.append(next_number)

with open('output.txt', 'w') as output_file:
    for number in fibonacci:
        output_file.write(str(number) + '\n')

