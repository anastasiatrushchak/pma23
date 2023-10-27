def tostr(dic):
    index = 1
    for key, val in dic.items():
        print(index," ", key, val)
        index+=1


dic = {
    "Pasternak": 12,
    "Predko": 13,
    "Mozil": 10
}

print("<-----------Початковий словник----------->")
tostr(dic)
print("<-----------Видалили елемент----------->")
try:
    del dic["Pasternak"]
    tostr(dic)
except Exception as e:
    print("Елемента нема")
print("<-----------Добавили елемент----------->")
dic["Flus"] = 9999
tostr(dic)
print("<-----------Змінили значення----------->")

dic["Mozil"] = 8888
tostr(dic)




