from calcfunctions import *

def doThing():
    print("Hello world")


def printnums() -> None:
    for i in range(10):
        print("i:",i)
    pass


def main():
    doThing()
    printnums()
    a = add(1, 2)
    q, r = divmod2(5,10)
    print(q, r)
    pass

if __name__ == "__main__":
    main()
