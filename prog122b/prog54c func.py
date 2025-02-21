def circleMath(rad):
    area = (rad**2)*3.14159
    circum = 2 * 3.14159 * rad
    return area, circum




def main():
    radi = int(input("Input radius"))
    area , circum = circleMath(radi)
    print(f"area= {area}")
    print(f"circumfrence= {circum}")

    pass
# Blank Line


if __name__ == "__main__":
    main()


