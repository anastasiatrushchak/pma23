class Lot:
    def __init__(self, destination, number, type):
        self.destination = destination
        self.number = number
        self.type = type
    def __str__(self):
        return f"name: {self.destination}, number: {self.number}, type: {self.type}"

def from_file(filename):
    with open(filename, mode="r")as readfile:
        lines = readfile.readlines()
    my_list = []
    for line in lines:
        string = ''
        attributes = []
        for letter in line:
            if letter == " ":
                attributes.append(string)
                string = ""
            else:
                if letter != '\n':
                    string += letter
        attributes.append(string)
        my_list.append(Lot(attributes[0], attributes[1], (attributes[2])))
    return my_list
def get_same_city(list, input_str):
    my_list = []
    for lot in list:
        if input_str == lot.destination:
            my_list.append(lot)
    return my_list

if __name__ == "__main__":
    my_list = from_file("file.txt")
    for lot in my_list:
        print(lot)

    destination = input("Ведіть назву призначення: ") # Київ
    my_list_search = get_same_city(my_list, destination)
    if len(my_list_search) != 0:
        print("Пошук: ")
        for lot in my_list_search:
            print(lot)
    else:
        print("Список пустий")
