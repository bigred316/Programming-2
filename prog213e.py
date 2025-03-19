def main():
    try:
        group1 = 0
        group2 = 0
        group3 = 0
        group4 = 0
        group5 = 0
        total = 0
        with open("Langdat/prog213e.dat", "r") as f:
            for line in f:
                if int(line) < 20:
                    group1 += 1
                elif int(line) in range(20, 40):
                    group2 += 1
                elif int(line) in range(40, 60):
                    group3 += 1
                elif int(line) in range(60, 80):
                    group4 += 1
                elif int(line) >= 80:
                    group5 += 1
                total = group1+group2+group3+group4+group5
            print("Langner Family")
            print("Age Group\tDistribution\tPecentage")
            print(f"<20\t\t\t{group1}\t\t\t\t{round(100*(group1/total),1)}")
            print(f"20-39\t\t{group2}\t\t\t\t{round(100*(group2/total),1)}")
            print(f"40-59\t\t{group3}\t\t\t\t{round(100*(group3/total),1)}")
            print(f"60-79\t\t{group4}\t\t\t\t{round(100*(group4/total),1)}")
            print(f">79\t\t\t{group5}\t\t\t\t{round(100*(group5/total),1)}")







    except OSError as e:
        print("Error", e)

    pass
# Blank Line


if __name__ == "__main__":
    main()
