class Worker:
    def __init__(self, name, position, year):
        self.name = name
        self.position = position
        self.year = year
    def __str__(self):
        return f"Прізвище: {self.name}, Посада: {self.position}, рік:{self.year}"

def from_file(filename):
    with open(filename, mode="r")as readfile:
        lines = readfile.readlines()
    my_list = []
    for line in lines:
        string = ''
        attributes = []
        for a in line:
            if a == " ":
                attributes.append(string)
                string = ""
            else:
                string += a
        attributes.append(string)
        my_list.append(Worker(attributes[0], attributes[1], int(attributes[2])))
    return my_list

if __name__ == "__main__":
    my_list = from_file("file.txt")
    for element in my_list:
        print(element)

    temp = input("Ведіть число: ") # Ведіть число 4
    for element in my_list:
        if int(temp) < (2024 - element.year):
            print(element)