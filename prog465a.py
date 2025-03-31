from random import randint
#import numpy as np

def printMatrix(mat):
    for row in mat:
        for num in row:
            print(f"{num:3d}", end="")
        print()

def max_matricies(mat1, mat2):
    rows = len(mat1)
    cols = len(mat1[0])
    mat_out = [[0]*cols  for _ in range(rows)]
    for r in range(rows):
        for c in range(cols):
            mat_out[r][c] = max(mat1[r][c] , mat2[r][c])
    return mat_out


def main():
    mat1 = []
    mat2=[]
    for r in range(5):
        row1 = []
        row2 = []
        for c in range(5):
            row1.append(randint(-50, 99))
            row2.append(randint(-50, 99))
        mat1.append(row1)
        mat2.append(row2)
    print("Matrix 1:")
    printMatrix(mat1)
    print("\nMatrix 2:")
    printMatrix(mat2)

    mat_max = max_matricies(mat1, mat2)
    print("\nLargest elements:")
    printMatrix(mat_max)

if __name__ == "__main__":
    main()


