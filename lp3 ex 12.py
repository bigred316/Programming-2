class Budget:
    def __init__(self, food, clothing, rent, entertainment):
        self.food = food
        self.clothing = clothing
        self.rent = rent
        self.entertainment = entertainment
        self._budget = 0
        self._percents = [0]*4

    def _get_percent(self, number):
        return round((number/ self._budget) * 100, 2)

    def calculate(self):
        self._budget = self.food + self.clothing + self.rent +self.entertainment
        self._percents[0] = self._get_percent(self.food)
        self._percents[1] = self._get_percent(self.clothing)
        self._percents[2] = self._get_percent(self.rent)
        self._percents[3] = self._get_percent(self.entertainment)

    def display(self):
        print("Category\t\tBudget")
        print(f"Food \t\t\t{self._percents[0]}%")
        print(f"Clothes \t\t{self._percents[1]}%")
        print(f"Rent \t\t\t{self._percents[2]}%")
        print(f"Entertainment \t{self._percents[3]}%")

def main():
    print("Enter amount spent last month on the following items")
    food = float(input("Food$"))
    clothes = float(input("Clothes$"))
    rent = float(input("Rent$"))
    entertainment = float(input("Float$"))
    print()

    spending = Budget(food, clothes, rent, entertainment)
    spending.calculate()
    spending.display()
    pass


if __name__ == "__main__":
    main()
