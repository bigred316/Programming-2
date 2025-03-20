class Circle:
    def __init__(self, radius):
        self.radius = radius
        self.area = 0
        self.circum = 0

    def circleMath(self):
        self.area = (self.radius**2)*3.14159
        self.circum = 2 * 3.14159 * self.radius




    def __str__(self):
        return f"Area = {self.area} and Circumference = {self.circum}"
