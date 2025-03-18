from cl701g import *
def main():
    try:
        people: list[Person] = []
        with open("../Langdat/prog701g.dat", "r") as f:
            num = int(f.readline())
            while num != 99:
                fn = f.readline()
                ln = f.readline()
                if num  == 1:
                    gpa = float(f.readline())
                    p = Student(fn, ln, gpa)
                    people.append(p)
                elif num == 2:
                    numstu = int(f.readline())
                    p = Teacher(fn, ln, numstu)
                    people.append(p)
                elif num == 3:
                    favword = f.readline().strip()
                    p = Admin(fn,ln,favword)
                    people.append(p)
                num  = int(f.readline())
            tot = 0
            cnt = 0
            tot_stus = 0
            largest = ""
            smallest = "hgaipfjdfhgjkdfhjklsghgudryhtsentghdfjkyhg9dfdjfdjfdfjkfjkfjfkfjkfjkfjkfjkfjkfjkfjkfjkfjkfjkfjkfjkfjkfjkfjkfjkfjkfjkfjkfjkfjkfjkfjkfjk"
            for person in people:
                if isinstance(person, Student):
                    tot += person.gpa
                    cnt += 1
                elif isinstance(person, Teacher):
                    tot_stus += person.numstu
                elif isinstance(person, Admin):
                    fw = person.favword
                    if len(fw) < len(smallest):
                        smallest = fw
                    if len(fw) > len(largest):
                        largest = fw
        print("Average student GPA: ", round(tot/cnt, 2))
        print("Total number of students taught", tot_stus)
        print("Smallest favorite admin word: ", smallest)
        print("Largest favorite admin word: ", largest)

    except OSError as e:
        print("Error", e)

    pass
# Blank Line
if __name__ == "__main__":
    main()

































