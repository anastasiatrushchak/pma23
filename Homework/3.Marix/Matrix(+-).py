def print_matrix(matrix):
    for i in matrix:
        print(i)
MATRIX_FIRST_INPUT='matriмx1.txt'
MATRIX_SECOND_INPUT='matrix2.txt'
MATRIX_RESULT='matrix_rez.txt'

matrix1=[]
matrix2=[]

try:
    with open(MATRIX_FIRST_INPUT, "r") as lines:
        lines = lines.readlines()

        for line in lines:
            row = [float(x) for x in line.split()]
            matrix1.append(row)
except FileNotFoundError:
    print("Файл " + MATRIX_FIRST_INPUT + "не знайдено")
    exit(-1)

try:
    with open(MATRIX_SECOND_INPUT, "r") as lines:
        lines = lines.readlines()

        for line in lines:
            row = [float(x) for x in line.split()]
            matrix2.append(row)
except FileNotFoundError:
    print("Файл " + MATRIX_SECOND_INPUT + "не знайдено")
    exit(-1)
try:
    matrix_sum = []
    for i in range(max(len(matrix2), len(matrix1))):
        row_matrix_rez=[]
        for j in range(max(len(matrix2[0]), len(matrix1[0]))):
            row_matrix_rez.append(float(matrix1[i][j]) + float(matrix2[i][j]))
        matrix_sum.append(row_matrix_rez)



    matrix_difference = []
    for i in range(len(matrix2)):
        row_matrix_rez=[]
        for j in range(len(matrix2[0])):
            row_matrix_rez.append(int(matrix1[i][j])-int(matrix2[i][j]))
        matrix_difference.append(row_matrix_rez)

    with open(MATRIX_RESULT, 'w') as file:
        file.write("Додавання:\n")
        for i in matrix_sum:
            file.write(str(i)+'\n')

        file.write("Віднімання:\n")
        for i in matrix_difference:
            file.write(str(i)+'\n')

except IndexError:
    print("неможливо додати і відняти матриці")



