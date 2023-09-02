import Constants
with open (Constants.input, 'r') as fileRead:
   array = fileRead.readline().split(Constants.space)
   array = [float(i) for i in array if i.isdigit()]
   const = 8
   for i in range(0, const):
       array.append(array[i] + array[i+1])
with open (Constants.output, 'w') as fileWrite:
   fileWrite.write(str(array))