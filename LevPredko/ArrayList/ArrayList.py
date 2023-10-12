class ArrayList:
    def __init__(self, arr=[]):
        self.__list = arr
        self.__free_cells = arr.count(None) if arr else 0

    def __increase_len(self):
        add = int(1.5 * len(self.__list) + 1)
        self.__list += [None] * add
        self.__free_cells = add

    def add(self, new_element):
        if isinstance(new_element, list):
            for element in new_element:
                self.add(element)
        else:
            if new_element is not None:
                if self.__free_cells == 0:
                    self.__increase_len()
                for i in range(len(self.__list)):
                    if self.__list[i] is None:
                        self.__list[i] = new_element
                        self.__free_cells -= 1
                        return

    def print_elements(self):
        print("arr:", self.__list)
        print("len:", len([item for item in self.__list if item is not None]))
        print("free cells:", self.__free_cells)
        print("capacity:", len(self.__list))  # Додано вивід розміру (capacity)

    def delete_element(self, index):
        try:
            if index >= len(self.__list) or index < 0:
                raise Exception("Error! Index out of range!")

            if self.__list[index] is not None:
                for i in range(index, len(self.__list) - 1):
                    self.__list[i] = self.__list[i + 1]
                self.__list.pop()
                self.__free_cells += 1
        except Exception as err:
            print(err)

    def clear(self):
        self.__list = []
        self.__free_cells = 0

myList = ArrayList([1, 2, 3])
myList.add([4 , 4, 5, 63, 4, 2])
myList.print_elements()

myList.delete_element(0)
myList.print_elements()

myList.add(6)
myList.print_elements()

myList.clear()
myList.print_elements()
