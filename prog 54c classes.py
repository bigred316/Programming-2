from cl54c import Circle
def main():
    rad = float(input("What is the radius of the circle"))
    circ= Circle(rad)
    circ.circleMath()

    print(str(circ))

if __name__ == "__main__":
    main()
