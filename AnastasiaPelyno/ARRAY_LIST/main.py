class ArrayList:
    def __init__(self, array=[]):
        self.len = len(array)
        self.size = len(array)
        self.array = array
        self.resize()

    def __str__(self):
        return str([x for x in self.array[:self.size]])

    def resize(self):
        self.len = int(1.5 * self.len) + 1
        new_array = [None] * self.len
        for i in range(self.size):
            new_array[i] = self.array[i]
        self.array = new_array

    def add(self, element):
        if self.size >= self.len:
            self.resize()
        self.array[self.size] = element
        self.size += 1

    def delete(self, index):

        if index < 0 or index > self.size:
            print("Invalid index. Deletion failed.")
        else:
            for i in range(index, self.size - 1):
                self.array[i] = self.array[i + 1]
            self.array[self.size - 1] = None
            self.size -= 1

    def insert(self, index, element):
        if self.size == self.len:
            self.resize()
        for i in range(self.size, index, -1):
            self.array[i] = self.array[i - 1]
        self.array[index] = element
        self.size += 1

    def clear(self):
        self.size = 0
        self.array = [None] * self.len

    def printed(self):
        #print(45 * '-_')
        print("ArrayList:", self.array)
        print(45 * '-_')


'''arr = ArrayList()
while True:
    print("ArrayList MENU:")
    print("1. Add")
    print("2. Delete")
    print("3. Insert")
    print("4. Clear")
    print("5. Exit")
    print(15 * '-_')
    choice = input("Enter your choice: ")

    try:
        choice = int(choice)
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue

    if choice == 1:
        element = input("Enter the element to add: ")
        arr.add(element)
        arr.printed()
    elif choice == 2:
        index = input("Enter the index to delete: ")
        try:
            index = int(index)
            arr.delete(index)
            arr.printed()
        except IndexError:
            print("Invalid index. Deletion failed.")
    elif choice == 3:
        index = input("Enter the index to insert: ")
        element = input("Enter the element to insert: ")
        try:
            index = int(index)
            arr.insert(index, element)
            arr.printed()
        except IndexError:
            print("Invalid index or element. Insertion failed.")
    elif choice == 4:
        arr.clear()
        arr.printed()
    elif choice == 5:
        print("Thank you for using program!")
        break
    else:
        print("Invalid choice. Please enter a valid menu option.")'''

arr=[1,28,5,12,3,4,5,4,4,4,7,8,7,8,76,5,4,3,20,9,7,4,3]
array_list=ArrayList(arr)
print("-------Original ArrayList-------")
array_list.printed()
array_list.add(10)
print("-------To ArrayList add 10 at the end-------")
array_list.printed()
try:
    array_list.delete(2)
except IndexError:
    print("Invalid index. Deletion failed.")
print("-------From ArrayList delete element on 2 position-------")
array_list.printed()
print("-------From ArrayList we try delete element on 58 position,which is not exist-------")
try:
    array_list.delete(58)
    array_list.printed()

except IndexError:
    print("Invalid index. Deletion failed.")
try:
    array_list.insert(0,18)
    print("-------To ArrayList we add element 18 on 0 position-------")
    array_list.printed()
except IndexError:
    print("Invalid index or element. Insertion failed.")
print("-------To ArrayList we try to add element 13 on 28 position, which is not exist-------")
try:
    array_list.insert(54,13)
    array_list.printed()
except IndexError:
    print("Invalid index or element. Insertion failed.")
array_list.clear()
print("-------ArrayList is cleared-------")
array_list.printed()
