INPUT='input.txt'
OUTPUT='output.txt'
STEPS='steps.txt'
try:
    with open(INPUT, 'r') as file_input:
        arr = file_input.read().split()
except FileNotFoundError:
    print('File Not Found')
try:
    with open(STEPS, 'r') as file_steps:
        steps = int(file_steps.read())
except FileNotFoundError:
    print('File Not Found')
for i in range(2):
    arr[i]=float(arr[i])
for i in range(2,steps):
    arr.append(arr[i-1]+arr[i-2])
with open(OUTPUT, 'w') as file_output:
    file_output.write(str(arr))
