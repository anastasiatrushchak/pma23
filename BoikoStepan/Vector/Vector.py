f_Vector = []
s_Vector = []

with open('Fvector.txt', 'r') as firstFileVector:
    for line in firstFileVector:
        values = line.strip().split()
        for value in values:
            f_Vector.append(int(value))

with open('Svector.txt', 'r') as secondFileVector:
    for line in secondFileVector:
        values = line.strip().split()
        for value in values:
            s_Vector.append(int(value))

 

vector_Sum = []
for i in range(len(f_Vector)):
    vector_Sum.append(f_Vector[i] + s_Vector[i])
print("Vector sum:\n",vector_Sum)

vector_Sub = []
for i in range(len(f_Vector)):
    vector_Sub.append(f_Vector[i] - s_Vector[i])
print("Vector sub:\n",vector_Sub)

vector_Mult = []
for i in range(len(f_Vector)):
    vector_Mult.append(f_Vector[i] * s_Vector[i])
print("Vector skalar:\n",vector_Mult)

vector_Div = []
for i in range(len(f_Vector)):
    vector_Div.append(f_Vector[i] / s_Vector[i])
print("Vector div:\n",vector_Div)

with open('OutputVector.txt', 'w') as file:
    file.write("Vector Sum:\n")
    file.write(str(vector_Sum) + '\n')
    file.write("Vector Sub:\n")
    file.write(str(vector_Sub) + '\n')
    file.write("Vector Skalar:\n")
    file.write(str(vector_Mult) + '\n')
    file.write("Vector Div:\n")
    file.write(str(vector_Div) + '\n')