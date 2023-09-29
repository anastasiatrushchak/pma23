try:
    f_Matrix = []
    s_Matrix = []

    with open('FMatrix.txt', 'r') as firstFileMatrix:
        for line in firstFileMatrix:
            row = [int(x) for x in line.split()]
            f_Matrix.append(row)

    with open('SMatrix.txt', 'r') as secondFileMatrix:
        for line in secondFileMatrix:
            row = [int(x) for x in line.split()]
            s_Matrix.append(row)
except Exception as e:
    print("error",e)






for row in range(len(f_Matrix)):
    print((str(f_Matrix[row]) ))
print()
for row in range(len(s_Matrix)):
    print((str(s_Matrix[row])))
print()
matrix_Sum = []
for i in range(len(f_Matrix)):
        row = []
        for j in range(len(f_Matrix[0])):
            row.append(f_Matrix[i][j] + s_Matrix[i][j])
        matrix_Sum.append(row)

matrix_Sub = []
for i in range(len(f_Matrix)):
        row = []
        for j in range(len(f_Matrix[0])):
            row.append(f_Matrix[i][j] - s_Matrix[i][j])
        matrix_Sub.append(row)

print(matrix_Sum)
print(matrix_Sub)


with open('OutputMatrix.txt', 'w') as file:
    file.write("Matrix Sum:\n")

    for row in range(len(matrix_Sum)):
        file.write(str(matrix_Sum[row]) + '\n')

    file.write("Matrix Subtract:\n")
    for row in range(len(matrix_Sub)):
        file.write(str(matrix_Sub[row]) + '\n')

