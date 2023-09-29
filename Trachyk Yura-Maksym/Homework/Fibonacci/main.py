# Реалізувати алгоритм Фібоначі. Алгоритм Фібоначі будує ряд Фібоначі.
# Ряд Фібоначі це такий ряд в якою кожний наступний елемент дорівнює сумі двох попередніх.
# Стандартний ряд Фібоначі: 0, 1, 1, 2, 3, 5, 8, 13, 21 .....

F1 = "number.txt"
F2 = "output.txt"
N = 8

with open(F1, "r") as number_file:
    array = number_file.readline().split()
for i in range(0, len(array)):
    array[i] = int(array[i])
for i in range(0, N):
    array.append(array[i-1] + array[i-2])
with open(F2, "w") as output_file:
    output_file.write(str(array))
