from cllp32 import Pizza

def main():
    pizza = Pizza(float(input("What diameter pizza do you want?")))
    pizza.costCalc()
    print(str(pizza))

if __name__ == "__main__":
    main()
