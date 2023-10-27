from Vasylyshyn_Dmytro.abstraction.Shape import Shape


class Colabs(Shape):
    def __init__(self, shape, color):
        super().__init__(color)
        self.shape = shape

    def __str__(self):
        return (

            "---------------------------------------------------------------------------------------------\n"
                f"| {self.shape.__class__.__name__:<15} | {self.color.apply_color():<15} | "
                f"Area: {self.calculate_area():<10.2f} | Perimeter: {self.calculate_perimeter():<10.2f} |\n"
            "---------------------------------------------------------------------------------------------"

        )

    def calculate_area(self):
        return self.shape.calculate_area()

    def calculate_perimeter(self):
        return self.shape.calculate_perimeter()

    def get_calculate_perimeter(self):
        return ( f"perimetr: {self.calculate_perimeter()}\n")

    def get_calculate_area(self):
        return (f"area: {self.calculate_area()}\n")
    def apply_color(self):
        return (
            f"{self.shape.__class__.__name__} with {self.color.apply_color()} color"
            "\n"
            "------------------------------------------------"

        )