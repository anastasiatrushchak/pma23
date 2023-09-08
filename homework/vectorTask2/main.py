import constants

with open(constants.INPUT_FILE, 'r') as file:
    line = file.readline()
    vector_a = line.strip().split(constants.SEPARATOR)
    line = file.readline()
    vector_b = line.strip().split(constants.SEPARATOR)

for num in range(0, len(vector_a)):
    vector_a[num] = float(vector_a[num])

for num in range(0, len(vector_b)):
    vector_b[num] = float(vector_b[num])

print("Vector A:", vector_a)
print("Vector B:", vector_b)

print("Choose operation (+,-,/,*):", end=' ')

def add(vector_a, vector_b):
    vector_c = []
    for i in range(len(vector_a)):
        vector_c.append(vector_a[i] + vector_b[i])
    print("Result:", vector_c)
    with open(constants.OUTPUT_FILE, 'w') as file:
        file.write(str(vector_c))

def subtract(vector_a, vector_b):
    vector_c = []
    for i in range(len(vector_a)):
        vector_c.append(vector_a[i] - vector_b[i])
    print("Result:", vector_c)
    with open(constants.OUTPUT_FILE, 'w') as file:
        file.write(str(vector_c))

def multiply(vector_a,  vector_b):
    vector_c = []
    for i in range(len(vector_a)):
        vector_c.append(vector_a[i] * vector_b[i])
    print("Result:", vector_c)
    with open(constants.OUTPUT_FILE, 'w') as file:
        file.write(str(vector_c))

def divide(vector_a, vector_b):
    vector_c = []
    for i in range(len(vector_a)):
        vector_c.append(vector_a[i] / vector_b[i])
    print("Result:", vector_c)
    with open(constants.OUTPUT_FILE, 'w') as file:
        file.write(str(vector_c))

match input():
    case '+':
        add(vector_a, vector_b)
    case '-':
        subtract(vector_a, vector_b)
    case '*':
        print(multiply(vector_a, vector_b))
    case '/':
        print(multiply(vector_a, vector_b))
