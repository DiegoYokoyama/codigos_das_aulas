from shape import Shape

class Circle(Shape):
    def __init__(self, radius, color):
        super().__init__(color)
        self.radius = radius

    def calculate_area(self):
        return 3.14159 * self.radius * self.radius
