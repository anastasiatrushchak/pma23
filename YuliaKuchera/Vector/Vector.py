def exist(filename):
    try:
        with open(filename, 'r') as file:
            print("Файл існує.")
            if file.read() =="":
                print("файл порожній")
            else:
                print("файл не порожній")
    except FileNotFoundError:
        print("Файл не існує.")

exist("inputV.txt")
exist("outputV.txt")

with open('inputV.txt', 'r') as file:
    lines = file.readlines()
    VectorFirst = list([float(x) for x in lines[0].strip().split()])
    VectorSecond = list([float(x) for x in lines[1].strip().split()])
result_add = []
for i in range(3):
    result_add.append(VectorFirst[i] + VectorSecond[i])
result_sub = []
for j in range(3):
    result_sub.append(VectorFirst[j] - VectorSecond[j])
result_mult = []
for k in range(3):
    result_mult.append(VectorFirst[k] * VectorSecond[k])
result_div = []
for l in range(3):
    try:
        result_div.append(VectorFirst[l] / VectorSecond[l])
    except ZeroDivisionError:
        print("Ділення на 0")

with open("outputV.txt", 'w') as f:
    print(result_add, file = f)
    print(result_sub, file = f)
    print(result_mult, file = f)
    print(result_div, file = f)

