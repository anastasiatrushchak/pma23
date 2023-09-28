MATRIX_ONE = 'matrix_1.txt'
MATRIX_TWO='matrix_2.txt'
RESULT_FILE='result.txt'
MODE_READ='r'
MODE_WRITE='w'
FILE_ERROR='File Not Found'


def actions(str1,str2):
    file.write(str1)
    for i in matrix_one:
        file.write(str(i) + '\n')
    file.write(str2 + '\n')
    for i in matrix_two:
        file.write(str(i) + '\n')
    file.write('=' + '\n')


def reading(matrix_file, mode, matrix):
    with open(matrix_file, mode) as file:
        for line in file:
            row=[int(i) for i in line.split()]
            matrix.append(row)


matrix_one=[]
try:
    reading(MATRIX_ONE,MODE_READ,matrix_one)
except FileNotFoundError:
    print(FILE_ERROR)
matrix_two=[]
try:
    reading(MATRIX_TWO,MODE_READ,matrix_two)
except FileNotFoundError:
    print(FILE_ERROR)
res_add=[]
for i in range(len(matrix_one)):
    row = []
    for j in range(len(matrix_one[0])):
        row.append(matrix_one[i][j] + matrix_two[i][j])
    res_add.append(row)
res_sub=[]
for i in range(len(matrix_one)):
    row = []
    for j in range(len(matrix_one[0])):
        row.append(matrix_one[i][j] - matrix_two[i][j])
    res_sub.append(row)
try:
    with open(RESULT_FILE,MODE_WRITE) as file:
        actions('Addition:\n','+')
        for i in res_add:
            file.write(str(i)+'\n')
        actions('Substraction\n','-')
        for i in res_sub:
            file.write(str(i)+'\n')
except FileNotFoundError:
    print(FILE_ERROR)
