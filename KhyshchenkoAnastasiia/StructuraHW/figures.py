# Основний клас для фігур
class Figure:
    def __init__(self, color):
        self.color = color

    def draw(self):
        pass

    def get_perimeter(self):
        pass

    def get_area(self):
        pass


# Клас для кола, успадковує властивості від Figure
class Circle(Figure):
    def __init__(self, radius, color):
        super().__init__(color)
        self.radius = radius

    def draw(self):
        return f"Малюємо коло з радіусом {self.radius}, кольору {self.color.fill_color()}."

    def get_perimeter(self):
        return 2 * 3.14 * self.radius

    def get_area(self):
        return 3.14 * (self.radius ** 2)


# Клас для прямокутника, успадковує властивості від Figure
class Rectangle(Figure):
    def __init__(self, length, width, color):
        super().__init__(color)
        self.length = length
        self.width = width

    def draw(self):
        return f"Малюємо прямокутник зі сторонами {self.length} і {self.width}, кольору {self.color.fill_color()}."

    def get_perimeter(self):
        return 2 * (self.length + self.width)

    def get_area(self):
        return self.length * self.width


# Клас для квадрата, успадковує властивості від Figure
class Square(Figure):
    def __init__(self, side, color):
        super().__init__(color)
        self.side = side

    def draw(self):
        return f"Малюємо квадрат зі стороною {self.side}, кольору {self.color.fill_color()}."

    def get_perimeter(self):
        return 4 * self.side

    def get_area(self):
        return self.side ** 2
