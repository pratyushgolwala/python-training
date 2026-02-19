#Q1

from math import sqrt


def matrix(rows, cols):
    mat = []
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(f"{i*cols + j}")
        mat.append(row)
    for row in mat:
        print(" ".join(row))
    print(mat)
        
matrix(3,3)




        





