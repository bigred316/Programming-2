from voidfunctions import *

def calcArea(len, width) -> int:
    return len * width

def calcPerim(len: int, wid: int) -> int:
    return 2*len + 2*wid

def areaPerim(len, wid):
    area = calcArea(len, wid)
    perim = calcPerim(len, wid)
    return(perim, area)

def main():
    doThing()
    len = int(input("Enter Length"))
    wid = int(input("Enter Width"))
    p , a = areaPerim(len, wid)
    print(f"Perimeter: {p}\nArea: {a}")

if __name__ == "__main__":
    main()
