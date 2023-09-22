MATRIX_ONE='matrix_1.txt'
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
def reading(matrix_file,mode,matrix):
    with open(matrix_file, mode) as file:
        for line in file:
            row=[int(i) for i in line.split()]
            matrix.append(row)
def mult(matr_one,matr_two):
    res = []
    for i in range(len(matr_one)):
        row = []
        for j in range(len(matr_two[0])):
            sum = 0
            for k in range(len(matr_two)):
                sum += matr_one[i][k] * matr_two[k][j]
            row.append(sum)
        res.append(row)
    return res
def det(matrix):
    n = len(matrix)
    if n == 1:
        return matrix[0][0]
    elif n == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    else:
        determinant = 0
        for j in range(n):
            submatrix = [[matrix[i][k] for k in range(n) if k != j] for i in range(1, n)]
            sign = (-1) ** j
            determinant += sign * matrix[0][j] * det(submatrix)
        return determinant
def algebraic_dopovnenia(matrix):
    n = len(matrix)
    alg_dopov = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            submatrix = [[matrix[k][l] for l in range(n) if l != j] for k in range(n) if k != i]
            sign = (-1) ** (i + j)
            alg_dopov[j][i] = sign * det(submatrix)
    return alg_dopov
def inverse(matrix):
    determinant = det(matrix)
    alg_dopov = algebraic_dopovnenia(matrix)
    inverse_matrix=[]
    n=len(alg_dopov)
    for i in range(n):
        row=[]
        for j in range(n):
            row.append(alg_dopov[i][j]/determinant)
        inverse_matrix.append(row)
    return inverse_matrix
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
mult_res=mult(matrix_one,matrix_two)
try:
    deter=det(matrix_two)
    inverse_matrix = inverse(matrix_two)
    div_res = mult(matrix_one, inverse_matrix)
except ZeroDivisionError:
    print('Matrixes can not be divided')
    exit(-1)
try:
    with open(RESULT_FILE,MODE_WRITE) as file:
        actions('Multiplying:\n','*')
        for i in mult_res:
            file.write(str(i)+'\n')
        actions('Dividing:\n', '/')
        for i in div_res:
            file.write(str(i) + '\n')
except FileNotFoundError:
    print(FILE_ERROR)