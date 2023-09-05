import numpy as np
list1=[1,2,3,4]
list2=[1,2,3,4]

list1=np.array(list1)
list2=np.array(list2)
try:
    print("Сума:")
    rez = list1 + list2
    print(rez)

    print("Різниця:")
    rez = list1 - list2
    print(rez)

    print("Множення:")
    rez = list1 * list2
    print(rez)

    print("Ділення:")
    rez = list1 / list2
    print(rez)
except:
    print("Неможливо виконати дії з векторами")

