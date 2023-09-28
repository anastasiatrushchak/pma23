import shutil
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



def copy_file(source_path, destination_path):
    try:
        shutil.copy(source_path, destination_path)
        print(f"Файл {source_path} успішно скопійовано до {destination_path}")
    except Exception as e:
        print(f"Сталася помилка при копіюванні файлу: {e}")

source_file = "FMatrix.txt"  # Замініть на шлях до вашого вихідного файлу
destination_file = "Sos.txt"  # Замініть на шлях до вашого файлу призначення

copy_file(source_file, destination_file)
import os

def check_file_existence(file_path):
    if os.path.exists(file_path):
        print(f"Файл '{file_path}' існує.")
        if os.path.isfile(file_path):
            print(f"'{file_path}' - це файл.")
        elif os.path.isdir(file_path):
            print(f"'{file_path}' - це директорія.")
    else:
        print(f"Файл або директорія '{file_path}' не існує.")

path_to_check = input("Введіть шлях до файлу або директорії: ")
check_file_existence(path_to_check)
'''
os.path.abspath(path): Повертає абсолютний шлях до вказаного шляху path.

os.path.basename(path): Повертає ім'я базового файлу або директорії з вказаного шляху path.

os.path.dirname(path): Повертає ім'я батьківської директорії з вказаного шляху path.

os.path.exists(path): Перевіряє, чи існує файл або директорія за вказаним шляхом path, і повертає True або False.

os.path.isfile(path): Перевіряє, чи є об'єкт за вказаним шляхом path файлом, і повертає True або False.

os.path.isdir(path): Перевіряє, чи є об'єкт за вказаним шляхом path директорією, і повертає True або False.

os.path.join(path1, path2, ...): Об'єднує шляхи в один шлях, дотримуючись правильного розділення шляхів у залежності від операційної системи.

os.path.split(path): Розділяє шлях на кортеж, що містить ім'я директорії та ім'я файлу.

os.path.splitext(path): Розділяє шлях на кортеж, що містить ім'я файлу та розширення файлу.

os.path.getsize(path): Повертає розмір файлу в байтах для вказаного шляху path.

os.path.abspath(path): Перетворює відносний шлях в абсолютний.

os.path.exists(path): Перевіряє існування шляху або файлу.

os.path.realpath(path): Повертає канонічний (нормалізований) абсолютний шлях до вказаного шляху path.

os.path.commonprefix(list): Знаходить спільний префікс для списку шляхів.'''