from RostyslavPasternak.Homework.Homework_1.Exception import InvalidSize
def add(first_vector, second_vector):
    if len(first_vector) == len(second_vector):
        size = len(first_vector)
        result = [first_vector[i] + second_vector[i] for i in range(size)]
        return result
    raise InvalidSize()

def sub(first_vector, second_vector):
    if len(first_vector) == len(second_vector):
        size = len(first_vector)
        result = [first_vector[i] - second_vector[i] for i in range(size)]
        return result
    raise InvalidSize()

def mul(first_vector, second_vector):
    if len(first_vector) == len(second_vector):
        size = len(first_vector)
        result = [first_vector[i] * second_vector[i] for i in range(size)]
        return result
    raise InvalidSize()


def div(first_vector, second_vector):
    if len(first_vector) == len(second_vector):
        size = len(first_vector)
        result = [first_vector[i] / second_vector[i] for i in range(size)]
        return result
    raise InvalidSize()

def str_to_file(vector,file_name="result.txt"):
    with open(file_name, 'w') as writeFile:
        writeFile.write(str(vector))

with open("vector1.txt", 'r') as readFile:
    line = readFile.readline()

first_vector = line.split(" ")
first_vector = [float(i) for i in first_vector if i.isdigit()]
print("First vector: ")
print(first_vector)
with open("vector2.txt", 'r') as readFile:
    line = readFile.readline()

second_vector = line.split(" ")
second_vector = [float(i) for i in second_vector if i.isdigit()]
print("Second vector: ")
print(second_vector)

while True:
    try:
        result = None
        operator = int(input("1. add\n2. subtraction\n3. multiplication\n4. division\n0. Cancel\n"))
        if operator == 1:
            result = add(first_vector, second_vector)
        elif operator == 2:
            result = sub(first_vector,second_vector)
        elif operator == 3:
            result = mul(first_vector,second_vector)
        elif operator == 4:
            result = div(first_vector,second_vector)
        else:
            break
    except InvalidSize as e:
        print(e)

    print(result)
    str_to_file(result)


