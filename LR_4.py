import numpy as np
import math
def iter(matrix, approx, eps = 0.1): #МЕТОД ИТЕРАЦИЙ
    lam1 = 1000
    lam2 = 0
    X11 = []
    X12 = []
    while abs(lam1 - lam2) > eps:
        X11 = np.matmul(matrix, approx)
        lam1 = (X11[0][0] / approx[0][0])
        approx = X11
        X12 = np.matmul(matrix, approx)
        lam2 = X12[0][0] / approx[0][0]
        approx = X12
    vector = [0, 0, 0]
    lamb = [0, 0, 0]
    for i in range(3):
        vector[i] = X12[i][0]
        lamb[i] = X12[i][0] / X11[i][0]
    print(f"Метод итераций \nсобственный вектор: {vector} \nсобственное значение: {lamb}")

matrix = np.array([ [5, 1, 2],
                    [1, 4, 1],
                    [2, 1, 3]])
approx = np.array([[1],
                   [1],
                   [1]])

iter(matrix, approx)

matrix1 = np.array([ [2, -1, 1],
                    [-1, 2, -1],
                    [0, 0, 1]])
approx1 = np.array([[1],
                   [-1],
                   [1]])
iter(matrix1, approx1, eps = 0.0001)



def rot(A, eps = 0.001): #МЕТОД ВРАЩЕНИЯ
    maxi = A[0][1]
    x = 0
    y = 1
    for i in range(3):
        for j in range(i + 1, 3):
            if maxi < A[i][j]:
                maxi = A[i][j]
                x = i
                y = j
    k = 0
    vec = np.array([[1, 0, 0],
                    [0, 1, 0],
                    [0, 0, 1]])
    while maxi > eps:
        phi = math.atan((2 * maxi) / (A[x][x] - A[y][y])) / 2
        sin = math.sin(phi)
        cos = math.cos(phi)
        if k % 3 == 0:
            H = np.array([[cos, 0, -sin],
                          [0, 1, 0],
                          [sin, 0, cos]])
        elif k % 3 == 1:
            H = np.array([[cos, -sin, 0],
                          [sin, cos, 0],
                          [0, 0, 1]])
        elif k % 3 == 2:
            H = np.array([[1, 0, 0],
                          [0, cos, -sin],
                          [0, sin, cos]])
        Ht = np.transpose(H)
        A = Ht @ A @ H
        vec = vec @ H
        maxi = A[0][1]
        for i in range(3):
            for j in range(i + 1, 3):
                if maxi < A[i][j]:
                    maxi = A[i][j]
        k += 1
    vec1 = [vec[0][0], vec[1][0], vec[2][0]]
    vec2 = [vec[0][1], vec[1][1], vec[2][1]]
    vec3 = [vec[0][2], vec[1][2], vec[2][2]]
    lamb = [A[0][0], A[1][1], A[2][2]]
    print(f"Методом вращения\n"
          f"собственный вектор 1: {vec1}\n"
          f"собственный вектор 2: {vec2}\n"
          f"собственный вектор 3: {vec3}\n"
          f"собственные значения: {lamb}\n")

A = np.array([[5, 1, 2],
              [1, 4, 1],
              [2, 1, 3]])
rot(A)

