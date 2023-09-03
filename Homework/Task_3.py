list1=[1,2,3,4]
list2=[1,2,3,4]

sum=[]
multipliation=[]
difference=[]
divide=[]
for i in range(min(len(list1), len(list2))):
    sum.append(list1[i]+list2[i])
    difference.append(list1[i]-list2[i])
    multipliation.append(list1[i]*list2[i])
    divide.append(list1[i]/list2[i])
print("Сума:")
print(sum)

print("Різниця:")
print(difference)

print("Множення:")
print(multipliation)

print("Ділення:")
print(divide)

