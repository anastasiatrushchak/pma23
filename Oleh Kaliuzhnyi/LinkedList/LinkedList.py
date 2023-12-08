from Node import Node


class LinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def append(self, data):
        try:
            new_node = Node(data)
            if self.is_empty():
                self.head = new_node
                self.head.next = self.head
                self.head.prev = self.head
            else:
                last_node = self.head.prev
                last_node.next = new_node
                new_node.prev = last_node
                new_node.next = self.head
                self.head.prev = new_node
        except Exception as err:
            print(f"Error in append method: {err}")

    def insert(self, index, data):
        try:
            new_node = Node(data)
            if self.is_empty():
                if index == 0:
                    self.head = new_node
                    self.head.next = self.head
                    self.head.prev = self.head
                else:
                    raise IndexError("Index out of range. List is empty.")
                return
            if index == 0:
                self.append(data)
                self.head = new_node
                return

            current = self.head
            count = 0
            while count < index - 1 and current.next != self.head:
                current = current.next
                count += 1

            if count < index - 1:
                raise IndexError("Index out of range.")
                return

            new_node.next = current.next
            new_node.prev = current
            current.next.prev = new_node
            current.next = new_node
        except Exception as err:
            print(f"Error in insert method: {err}")

    def delete(self, index):
        try:
            if self.is_empty():
                raise IndexError("Cannot delete from an empty list.")

            if index == 0:
                if self.head.next == self.head:  # Only one element in the list
                    self.head = None
                else:
                    last_node = self.head.prev
                    self.head.next.prev = last_node
                    last_node.next = self.head.next
                    self.head = self.head.next
                return

            current = self.head
            count = 0
            while count < index and current.next != self.head:
                current = current.next
                count += 1

            if count < index:
                raise IndexError("Index out of range.")
                return

            current.prev.next = current.next
            current.next.prev = current.prev
        except Exception as err:
            print(f"Error in delete method: {err}")

    def print_list(self):
        try:
            if self.is_empty():
                print("Circular Doubly Linked List is empty.")
                return

            current = self.head
            while True:
                print(current.data, end=", ")
                current = current.next
                if current == self.head:
                    break
            print()
        except Exception as err:
            print(f"Error in display method: {err}")