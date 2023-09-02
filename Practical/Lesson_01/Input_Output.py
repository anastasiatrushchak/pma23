with open ('input.txt', 'r') as fileRead:
   array = fileRead.readline().split(" ")
   array = [float(i) for i in array if i.isdigit()]
   const = 8
   for i in range(0, const):
       array.append(array[i] + array[i+1])
with open ("output.txt", 'w') as fileWrite:
   fileWrite.write(str(array))