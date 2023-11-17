class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class ArrayList:
    def __init__(self):
        self.size = 0
        self.capacity = 10
        self.array = [None] * self.capacity

    def resize(self):
        new_capacity = int(1.5 * self.capacity) + 1
        new_array = [None] * new_capacity
        for i in range(self.size):
            new_array[i] = self.array[i]
        self.capacity = new_capacity
        self.array = new_array

    def add(self, element):
        if self.size == self.capacity:
            self.resize()
        self.array[self.size] = element
        self.size += 1

    def remove(self, element):
        if element in self.array:
            index = self.array.index(element)
            for i in range(index, self.size - 1):
                self.array[i] = self.array[i + 1]
            self.size -= 1
            self.array[self.size] = None

    def insert(self, index, element):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of bounds")
        if self.size == self.capacity:
            self.resize()
        for i in range(self.size, index, -1):
            self.array[i] = self.array[i - 1]
        self.array[index] = element
        self.size += 1

    def clear(self):
        self.size = 0
        self.capacity = 10
        self.array = [None] * self.capacity

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, element):
        new_node = Node(element)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def remove(self, element):
        current = self.head
        while current:
            if current.data == element:
                if current.prev:
                    current.prev.next = current.next
                else:
                    self.head = current.next
                if current.next:
                    current.next.prev = current.prev
                else:
                    self.tail = current.prev
                return
            current = current.next

    def insert(self, index, element):
        new_node = Node(element)
        current = self.head
        for i in range(index):
            if current:
                current = current.next
        if not current:
            raise IndexError("Index out of bounds")
        if current.prev:
            current.prev.next = new_node
            new_node.prev = current.prev
        else:
            self.head = new_node
        new_node.next = current
        current.prev = new_node

    def clear(self):
        self.head = None
        self.tail = None
        # Абстракція для фігур
class Shape:
    def __init__(self, color):
        self.color = color

    def draw(self):
        pass

    def compute_area(self):
        pass

    def compute_perimeter(self):
        pass

# Реалізація абстракції для кольорів
class Color:
    def fill_color(self):
        pass

# Реалізація кольору - червоний
class RedColor(Color):
    def fill_color(self):
        return "Red"

# Реалізація кольору - зелений
class GreenColor(Color):
    def fill_color(self):
        return "Green"

# Реалізація кольору - синій
class BlueColor(Color):
    def fill_color(self):
        return "Blue"

# Реалізація кола
class Circle(Shape):
    def __init__(self, color, radius):
        super().__init__(color)
        self.radius = radius

    def draw(self):
        return f"A {self.color.fill_color()} circle with radius {self.radius}"

    def compute_area(self):
        return 3.14 * self.radius * self.radius

    def compute_perimeter(self):
        return 2 * 3.14 * self.radius

# Реалізація прямокутника
class Rectangle(Shape):
    def __init__(self, color, width, height):
        super().__init__(color)
        self.width = width
        self.height = height

    def draw(self):
        return f"A {self.color.fill_color()} rectangle with width {self.width} and height {self.height}"

    def compute_area(self):
        return self.width * self.height

    def compute_perimeter(self):
        return 2 * (self.width + self.height)

# Реалізація квадрата
class Square(Shape):
    def __init__(self, color, side_length):
        super().__init__(color)
        self.side_length = side_length

    def draw(self):
        return f"A {self.color.fill_color()} square with side length {self.side_length}"

    def compute_area(self):
        return self.side_length ** 2

    def compute_perimeter(self):
        return 4 * self.side_length

# Приклад використання
red_color = RedColor()
green_color = GreenColor()

circle = Circle(red_color, 5)
rectangle = Rectangle(green_color, 4, 6)

print(circle.draw())
print(f"Area: {circle.compute_area()}")
print(f"Perimeter: {circle.compute_perimeter()}")

print(rectangle.draw())
print(f"Area: {rectangle.compute_area()}")
print(f"Perimeter: {rectangle.compute_perimeter()}")