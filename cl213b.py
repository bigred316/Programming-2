class Order:
    def __init__(self, amount):
        self.amount = int(amount)
        self.priceper = 0
        self.cost = 0


    def calcPrice(self):
        if self.amount in range(0, 100):
            self.priceper = 5.95
        elif self.amount in range(100, 200):
            self.priceper = 5.75
        elif self.amount in range(200, 300):
            self.priceper = 5.40
        elif self.amount >= 300:
            self.priceper = 5.15
        self.cost = round(self.priceper * self.amount,2)

    def __str__(self):
        return f"Price: ${self.priceper}\nTotal: ${self.cost}"

