import math

A = [[5, 0, 1, 11],
     [2, 6, -2, 8],
     [-3, 2, 10, 6]]
B = [[2, 1, 4, 16],
     [3, 2, 1, 10],
     [1, 3, 3, 16]]
def single_dev_Gaus(A): #Метод Гаусса единственного деления
    for i in range(3):
        temp = A[i][i]
        for j in range(i, 4):
            A[i][j] = A[i][j] / temp
        for x in range(i + 1, 3):
            temp = A[x][i]
            for y in range(i, 4):
                A[x][y] = A[x][y] - temp * A[i][y]
    x3 = A[2][3] / A[2][2]
    x2 = (A[1][3] - A[1][2] * x3) / A[1][1]
    x1 = (A[0][3] - A[0][2] * x3 - A[0][1] * x2) / A[0][0]
    print (f"Методом Гаусса единственного деления: x1={x1}, x2={x2}, x3={x3}")
single_dev_Gaus(B)
def choose_main_Gaus(A): #Метод Гаусса с выбором ведущего элемента по столбцам
    for j in range (3):
        for i in range(j + 1, 3):
            if A[j][j] < A[i][j]:
                for k in range(j, 4):
                    temp = A[j][k]
                    A[j][k] = A[i][k]
                    A[i][k] = temp
        temp = A[j][j]
        for x in range (j, 4):
            A[j][x] = A[j][x] / temp
        for x in range(j + 1, 3):
            temp = A[x][j]
            for y in range(j, 4):
                A[x][y] = A[x][y] - temp * A[j][y]
    x3 = A[2][3] / A[2][2]
    x2 = (A[1][3] - A[1][2] * x3) / A[1][1]
    x1 = (A[0][3] - A[0][2] * x3 - A[0][1] * x2) / A[0][0]
    print(f"Методом Гаусса с выбором ведущего элемента по столбцам: x1={x1}, x2={x2}, x3={x3}")

C = [[-3, 2.099, 6, 3.901],
     [5, -1, 5, 6],
     [10, -7, 0, 7]]

choose_main_Gaus(C)

D = [[2, 2, 10, 14],
     [10, 1, 1, 12],
     [2, 10, 1, 13]]

def simple_itr(A, eps = 0.01): #Методом простых итераций
    for j in range(3):
        for i in range(j + 1, 3):
            if A[j][j] < A[i][j]:
                for k in range(4):
                    temp = A[j][k]
                    A[j][k] = A[i][k]
                    A[i][k] = temp
    for i in range(3):
        temp = A[i][i]
        for j in range (3):
            A[i][j] = - A[i][j]/temp
        A[i][3] = A[i][3] / temp
        A[i][i] = 0
    a = 0
    b = 0
    for i in range (3):
        sum = 0
        for j in range (3):
            sum += abs(A[i][j])
        if sum > a:
            a = sum
        if A[i][3] > b:
            b = A[i][3]
    k = ((math.log10(eps) + math.log10(1-a) - math.log10(b)) / math.log10(a) - 1).__ceil__()
    OTV = [0,0,0]
    temp = [A[0][3], A[1][3], A[2][3]]
    for i in range (k+1):
        for j in range (3):
            OTV[j] = A[j][0]*A[0][3]+A[j][1]*A[1][3]+A[j][2]*A[2][3] + temp[j]
        for j in range (3):
            A[j][3] = OTV[j]
    x1 = OTV[0]
    x2 = OTV[1]
    x3 = OTV[2]
    print(f"Методом простых итераций с точностью eps = 0,01: x1={x1}, x2={x2}, x3={x3}")

simple_itr(D)