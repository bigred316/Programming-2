def main():
    #write mode
    with open("cool.txt" , "w") as f:
        f.write("cool\n")
        f.write("beans")
    #append mode
    with open("cool.txt" , "a") as f:
        f.write("\nwowzers!")
    #read (like a book)
    with open("cool.txt" , "r") as f:
        #print(f.readlines))
        for line in f:
            print(line, end= "")


    pass


if __name__ == "__main__":
    main()
