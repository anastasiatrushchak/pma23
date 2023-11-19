class Student:
    def __init__(self, first_name, course, avg_mark):
        if not (len(first_name) >= 3 and isinstance(first_name, str)):
            raise Exception('First name should be a string and have more than two letters')
        self.first_name = first_name

        if not (1 <= course <= 6 and isinstance(course, int)):
            raise Exception('Course should be in range from 1 to 6 and be int')
        self.course = course
        self.avg_mark = avg_mark

    def __str__(self):
        return f'First name:{self.first_name},  Course:{self.course}, Avg mark:{self.avg_mark}'


try:
    dict_s = dict()
    dict_s['vdfl'] = Student('dfvdf', 2, 2, 97)
    dict_s['Vovk'] = Student('xcsd', 3, 2, 67)
    dict_s['xcv'] = Student('xcvx', 1, 2, 89)
    dict_s['sdv'] = Student('vsdvs', 4, 2, 75)
    dict_s['sdvsd'] = Student('svsdv', 5, 2, 98)

    for k in dict_s:
        print(dict_s[k])

    dict_s['Vovk'].course = 3
    dict_s['sdv'] = Student('sddds', 2, 1, 51)

    dict_s.pop('xvkmlkknklnknlnln')

    for k, v in dict_s.items():
        print(k, ' - ', v)
except Exception as e:
    print(e)
