import json
class Student:
    def __init__(self, name, group, note):
        self.name = name
        self.group = group
        self.note = note
    def is_more_than5(self):
        return sum(self.note)/len(self.note) > 4.0
    def __str__(self):
        return f"name: {self.name}, group: {self.group}, note: {self.note}"

if __name__ =="__main__":
    with open("student.json", mode='r') as file:
        data = json.load(file)
        my_list = []
        for element in data:
            my_list.append(Student(element["name"], element["group"], element["note"]))

    for i in my_list:
        print(i)

    my_second_list = []
    for i in my_list:
        if i.is_more_than5():
            my_second_list.append(i)

    print("Відмінники: ")
    if len(my_second_list) > 0:
        for i in my_second_list:
            print(i)
    else:
        print("Нема відмінників")