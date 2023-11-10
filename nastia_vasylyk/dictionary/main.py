from Student import Student
try:
    dict_s = dict()
    dict_s['Vasylyk'] = Student('Nastia', 'Vasylyk', 2, 97)
    dict_s['Vovk'] = Student('Oleh', 'Vovk', 2, 67)
    dict_s['Melnyk'] = Student('Maria', 'Melnyk', 2, 89)
    dict_s['Kit'] = Student('Danylo', 'Kit', 2, 75)
    dict_s['Kohyt'] = Student('Yura', 'Kohyt', 2, 98)

    for k in dict_s: #перебираємо ключі
        print(dict_s[k]) #за допомогою ключа витягуємо значення

    dict_s['Vovk'].course = 3
    dict_s['Kit'] = Student('Marta', 'Kit', 1, 51)

    dict_s.pop('Kohyt')

    for k, v in dict_s.items(): #тут ми виводимо ключ-значення
        print(k, ' - ', v)
except Exception as e:
    print(e)