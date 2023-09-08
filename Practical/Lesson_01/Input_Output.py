import Constants
const = 8
with open (Constants.input, 'r') as fileRead:
   array = fileRead.readline().split(Constants.space)
   array = [float(i) for i in array if i.isdigit()]
   for i in range(0, const):
       array.append(array[i] + array[i+1])
with open (Constants.output, 'w') as fileWrite:
   fileWrite.write(str(array))