from cllp311 import Project
def main():
    design = float(input("How long did you spend designing the program?"))
    code = float(input("How long did you spend coding the program?"))
    debug = float(input("How long did you spend debugging the program?"))
    test = float(input("How long did you spend testing the program?"))
    program = Project(design,code,debug,test)
    program.percentCalc()
    print(str(program))
# Blank Line


if __name__ == "__main__":
    main()
