class Shape:
    def __init__(self, length, width):
        self.length= length
        self.width= width
        self._area = 0
        self._perim = 0

    def calculate(self):
        self._area = self.length * self.width
        self._perim = 2* self.length + self.width

    #accessor/getter method:(returns privates)
    def get_area(self):
            return self._area
    def get_perim(self)
            return self._perim


def main():
    length = int(input("Enter length"))
    width = int(input("enter width"))
    shape.calculate()
    print("Area: ", Shape.get_area())
    print("Perimeter: ", Shape.get_perim())
    shape = Shape(length, width) #call class constructor

    pass
# Blank Line


if __name__ == "__main__":
    main()
