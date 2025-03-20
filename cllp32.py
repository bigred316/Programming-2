class Pizza():
    def __init__(self, diameter):
        self.diameter = diameter
        self.cost = 0

    def costCalc(self):
        self.cost = 1 + 0.75 + (0.05 * self.diameter*self.diameter)

    def __str__(self):
        return f"Your pizza will cost ${round(self.cost,2)}"

