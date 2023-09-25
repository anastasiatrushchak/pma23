INPUT = 'inputVector.txt'
OUTPUT = 'outputVector.txt'
FILE_NOT_FOUND = 'file not found'
ZERO_DIVISION = 'division by zero'

try:
    with open(INPUT, 'r') as inpV:
        vectA = inpV.readline().split()
        vectA = [float(i) for i in vectA if i.isdigit()]
        vectB = inpV.readline().split()
        vectB = [float(i) for i in vectB if i.isdigit()]
except FileNotFoundError:
    print(FILE_NOT_FOUND)
    exit(-1)


def addition(vector_a, vector_b):
    result = []
    for i in range(len(vector_a)):
        result.append(vector_a[i]+vector_b[i])
    return result


def subtraction(vector_a, vector_b):
    result = []
    for i in range(len(vector_a)):
        result.append(vector_a[i]-vector_b[i])
    return result


def multiplication(vector_a, vector_b):
    result = []
    for i in range(len(vector_a)):
        result.append(vector_a[i]*vector_b[i])
    return result


def division(vector_a, vector_b):
    result = []
    try:
        for i in range(len(vector_a)):
            result.append(vector_a[i]/vector_b[i])
        return result
    except ZeroDivisionError:
        print(ZERO_DIVISION)
        exit(-1)


with open(OUTPUT, 'w') as out:
    out.write("Addition:\n")
    out.write(str(addition(vectA, vectB))+'\n')

    out.write("Subtraction:\n")
    out.write(str(subtraction(vectA, vectB)) + '\n')

    out.write("Multiplication:\n")
    out.write(str(multiplication(vectA, vectB)) + '\n')

    out.write("Division:\n")
    out.write(str(division(vectA, vectB)) + '\n')



