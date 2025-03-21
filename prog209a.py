from cl209a import numSort
def main():
    higher = 0
    lower = 0
    total = 0
    try:
        with open("../Langdat/prog 215a.dat", "r") as f:
            for line in f:
                line = numSort()
                line.Count()
                if str(line) == True:
                    higher += 1
                else:
                    lower += 1
                total += 1


    except OSError as e:
        print("Error", e)

    pass
# Blank Line


if __name__ == "__main__":
    main()
