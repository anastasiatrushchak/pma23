import numpy as np
try:
    with open("vect.input.txt", 'r') as f:
        vector = f.readline().split()
        vector2 = f.readline().split()
except FileNotFoundError:
    print("Error no file")
    exit(-1)
vector = [float(i) for i in vector if i.isdigit()]
vector2 = [float(i) for i in vector2 if i.isdigit()]
print("Addition of two vectors:")
suma = []
for i in range(len(vector)):
    suma.append(vector[i] + vector2[i])
print(suma)

print("Multiplication of two vectors:")
# mult = np.cross(vector, vector2)
# print(mult)

result = []
for i in range(0, len(vector)):
    result.append(vector[i] * vector2[i])
    print(result)

    print("Subtraction of two vectors:")
    sub = [vector[i] - vector2[i] for i in range(len(vector))]
print(sub)

# sub = np.subtract(vector, vector2)
# print(sub)

print("Division of two vectors")
# div = np.divide(vector, vector2)
# print(div)
division = []
for i in range(len(vector)):
    try:
        division.append(vector[i]/vector2[i])
    except ZeroDivisionError:
        print("Zero division")
        exit(-1)
print(division)



with open("vect.output.txt", 'w') as file:
    file.write("Suma: "+str(suma)+"\n")
    file.write("Division: "+str(division)+"\n")
    file.write("Multiply: "+str(result)+"\n")
    file.write("Subtraction: "+str(sub)+"\n")