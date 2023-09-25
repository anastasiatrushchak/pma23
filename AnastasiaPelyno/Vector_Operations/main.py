VECTORS_FILE='vectors.txt'
FILE_ERROR='File Not Found'

def smth(action,res):
    file.write(action)
    for i in res:
        file.write(str(i) + ' ')
    file.write('\n')
try:
    with open(VECTORS_FILE,'r') as file:
        lines=file.readlines()
        first_vector=[int(x) for x in lines[0].split()]
        vector2=[int(x) for x in lines[1].split()]
except FileNotFoundError:
    print(FILE_ERROR)

add_res=[first_vector[i]+vector2[i] for i in range(len(first_vector))]
sub_res=[first_vector[i]-vector2[i] for i in range(len(first_vector))]
mult_res=[first_vector[i]*vector2[i] for i in range(len(first_vector))]
try:
    div_res=[first_vector[i]/vector2[i] for i in range(len(first_vector))]
except ZeroDivisionError:
    print('Division by zero')
RESULT_FILE='result.txt'
try:
    with open(RESULT_FILE,'w') as file:
        smth("Addition:\n",add_res)
        smth("Substraction:\n",sub_res)
        smth("Multiplication:\n",mult_res)
        smth("Division:\n",div_res)

except FileNotFoundError:
    print(FILE_ERROR)
