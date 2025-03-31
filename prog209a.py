from cl209a import numSort
def main():
    higher = 0
    lower = 0
    total = 0
    try:
        with open("Langdat/prog215a.dat", "r") as f:
            for line in f:
                num = numSort(int(line))
                num.Count()
                if str(num) == "one":
                    higher += 1
                else:
                    lower += 1
                total += 1
            print(f"There are {higher} numbers higher than or equal to 500\nThere are {lower} numbers lower than 500\nThere are {total} numbers in the file")


    except OSError as e:
        print("Error", e)

    pass
# Blank Line


if __name__ == "__main__":
    main()
