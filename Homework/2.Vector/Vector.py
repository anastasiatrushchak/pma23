VECTOR_FIRST_FILE = 'VectorFirst.txt'
VECTOR_SECOND_FILE = 'VectorSecond.txt'
VECTOR_FILE_RESULT = 'VectorResult.txt'
mode = 'r'
separate = ','

try:
    with open(VECTOR_FIRST_FILE, mode) as file:
        vector_first = file.readline().split(separate)
        vector_first = [float(i) for i in vector_first]


except FileNotFoundError:
    print("Файл " + VECTOR_FIRST_FILE + " не зайдено.")
    exit(-1)

try:
    with open(VECTOR_SECOND_FILE, mode) as file:
        vector_second = file.readline().split(separate)
        vector_second = [float(i) for i in vector_second]
except FileNotFoundError:
    print("Файл " + VECTOR_SECOND_FILE + " не зайдено.")
    exit(-1)


try:
    sum = []
    multipliation = []
    difference = []
    divide = []
    for i in range(max(len(vector_first), len(vector_second))):
        sum.append(vector_first[i] + vector_second[i])
        difference.append(vector_first[i] - vector_second[i])
        multipliation.append(vector_first[i] * vector_second[i])
        divide.append(vector_first[i] / vector_second[i])

    with open(VECTOR_FILE_RESULT, 'w') as file:
        file.write("Додавання:\n" + str(sum)+'\n')
        file.write("Віднімання:\n" + str(difference)+'\n')
        file.write("Множення:\n" + str(multipliation) + '\n')
        file.write("Ділення:\n" + str(divide) + '\n')
except IndexError:

    print("Неможливо додати вектори розмірів " + str(len(vector_first)) + " і " + str(len(vector_second)))
    exit(-1)
except ZeroDivisionError:
    print("Неможливо ділити на нуль")

