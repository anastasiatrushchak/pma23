INPUT = 'input.txt'
try:
    with open(INPUT, 'r') as f:
        array = f.read().split()
    array = [float(i) for i in array if i.isdigit()]

    INPUT2 = 'lim.input.txt'
    with open(INPUT2, 'r') as file:
        lim = int(file.read())
except FileNotFoundError:
    print("No file found")

def fib(array, lim):
     next_num = array[len(array) - 1] + array[len(array) - 2]
     if next_num <= lim:
         array.append(next_num)
         return fib(array, lim)
     else:
         return array

f = fib(array, lim)






OUTPUT = 'output.txt'
with open (OUTPUT, 'w') as file:
        file.write(str(f))

# for i in range(2, 10):
    #     array.append((array[i-1]) + (array[i-2]))
