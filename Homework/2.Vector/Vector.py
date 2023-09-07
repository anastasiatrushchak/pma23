vector1=[]
vector2=[]

with open('vector1.txt', 'r') as file:
    line1=file.readline()
    for i in line1.split():
        vector1.append(float(i))
with open('vector2.txt', 'r') as file:
    line2 = file.readline()
    for i in line2.split():
        vector2.append(float(i))
if len(vector1)==len(vector2):
    sum=[]
    multipliation=[]
    difference=[]
    divide=[]
    for i in range(min(len(vector1), len(vector2))):
        sum.append(vector1[i]+vector2[i])
        difference.append(vector1[i]-vector2[i])
        multipliation.append(vector1[i]*vector2[i])
        divide.append(vector1[i]/vector2[i])
    with open("vector_rez.txt",'w') as file:
        file.write("Додавання:\n"+ str(sum)+'\n')
        file.write("Віднімання:\n" + str(difference)+'\n')
        file.write("Множення:\n" + str(multipliation) + '\n')
        file.write("Ділення:\n" + str(divide) + '\n')
else:
    with open("vector_rez.txt", 'w') as file:
        file.write("Неможливо виконати дії з векторами")

