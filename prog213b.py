from cl213b import Order

def main():
    amount = input("how many things would you like to buy")
    order = Order(amount)
    order.calcPrice()
    print(str(order))

if __name__ == "__main__":
    main()
