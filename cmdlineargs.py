import sys
def main(args):
    #c style main/entrypoint function
    if len(args) <= 0:
        print("Hello!")
        return
    print("Hello!", args[0])
    for arg in args:
        print(arg)
    pass
# Blank Line


if __name__ == "__main__":
    main(sys.argv[1:])
