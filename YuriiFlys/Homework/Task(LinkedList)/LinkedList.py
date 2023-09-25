class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        if not self.head:
            self.head = Node(data)
        else:
            node = self.head
            while node.next:
                node = node.next
            new_node = Node(data)
            node.next = new_node
            new_node.prev = node

    def remove(self, data):
        node = self.head
        while node:
            if node.data == data:
                if node.prev:
                    node.prev.next = node.next
                else:
                    self.head = node.next
                if node.next:
                    node.next.prev = node.prev
                return True
            node = node.next
        raise ValueError("Елемент не знайдено в списку")

    def insert(self, index, data):
        if index == 0:
            new_node = Node(data)
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        else:
            node = self.head
            for _ in range(index - 1):
                if not node:
                    return False
                node = node.next
            if not node:
                return False
            new_node = Node(data)
            new_node.next = node.next
            new_node.prev = node
            if node.next:
                node.next.prev = new_node
            node.next = new_node

    def clear(self):
        self.head = None

    def display(self):
        elements = []
        node = self.head
        while node:
            elements.append(node.data)
            node = node.next
        return elements

llist = LinkedList()
llist.append("A")
llist.append("B")
llist.append("C")
while True:
    try:
        print("1. Додати елемент в кінець списку")
        print("2. Видалити елемент зі списку")
        print("3. Вставити елемент за індексом")
        print("4. Очистити список")
        print("5. Показати список")
        print("6. Вийти")

        choice = int(input("Введіть ваш вибір: "))

        if choice == 1:
            data = input("Введіть дані: ")
            llist.append(data)
        elif choice == 2:
            data = input("Введіть дані для видалення: ")
            llist.remove(data)
        elif choice == 3:
            index = int(input("Введіть індекс: "))
            data = input("Введіть дані: ")
            llist.insert(index, data)
        elif choice == 4:
            llist.clear()
        elif choice == 5:
            print(llist.display())
        elif choice == 6:
            break
        else:
            raise ValueError("Невірний вибір. Будь ласка, введіть число від 1 до 6.")
    except ValueError as ve:
        print(f"Помилка вводу або елемент не знайдено: {ve}")
    except Exception as e:
        print(f"Сталася помилка: {e}")
