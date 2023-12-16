import math

import numpy as np

pol = np.array([1, 0, -1, 1])

def funk(x, pol):
    fun = 0
    for i in range (len(pol)):
        fun += pol[i]*x**(len(pol)-i-1)
    return fun
def der(pol):
    df = []
    for i in range(0, len(pol)-1):
        df.append(pol[i] * (len(pol) - 1 - i))
    return df
def met_Newton (x0, eps): #МЕТОД НЬЮТОНА
    pol1 = der(pol)
    pol2 = der(pol1)
    if funk(x0, pol)*funk(x0, pol2) <= 0:
        return "Неправильно подобран x0"
    x1 = x0 - funk(x0, pol) / funk(x0, pol1)
    while abs(x1 - x0) > eps:
        x0 = x1
        x1 = x0 - funk(x0, pol) / funk(x0, pol1)
    return x1
print (f"Метод Ньютона: х = {met_Newton(-2, 0.001)}")

def easy_met_Newtona(x0, eps): #УПРОЩЕННЫЙ МЕТОД НЬЮТОНА
    pol1 = der(pol)
    pol2 = der(pol1)
    f_pol1 = funk(x0, pol1)
    if funk(x0, pol) * funk(x0, pol2) <= 0:
        return "Неправильно подобран x0"
    x1 = x0 - funk(x0, pol) / f_pol1
    while abs(x1 - x0) > eps:
        x0 = x1
        x1 = x0 - funk(x0, pol) / f_pol1
    return x1
print (f"Упрощенный медот Ньютона: х = {easy_met_Newtona(-2, 0.001)}")


def met_New_Broid(x0, eps, c):
    pol1 = der(pol)
    pol2 = der(pol1)
    if funk(x0, pol) * funk(x0, pol2) <= 0:
        return "Неправильно подобран x0"
    x1 = x0 - funk(x0, pol) / funk(x0, pol1)
    while abs(x1 - x0) > eps:
        x0 = x1
        x1 = x0 - c*funk(x0, pol) / funk(x0, pol1)
    return x1
print (f"Метод Ньютона-Бройдена: х = {met_New_Broid(-2, 0.001, 1)}")

poli = np.array([3, -4, -8, 10, -7])
def met_Sec(x0, eps, psi):
    pol1 = (funk(x0, poli) - funk(x0 - psi, poli))/psi
    x1 = x0 - funk(x0, poli)/pol1
    while abs(x1 - x0) > eps:
        x0 = x1
        pol1 = (funk(x0, poli) - funk(x0 - psi, poli)) / psi
        x1 = x0 - funk(x0, poli) / pol1
    return x1
print(f"Метод секущих: х = {met_Sec(10, 0.001, 0.1)}")

def third():
    A = np.max(abs(poli[1:]))
    B = np.max(abs(poli[:-1]))
    left = 1/(1+B/abs(poli[-1]))
    right = 1+A/abs(poli[0])
    return (f"{left}<|x*j|<={right}")
print(f"Теорема 3:{third()}")

def fourth(x):
    n = -1
    for i in range (len(x)):
        if x[i]>0:
            n = i
            i+=1
            while i<len(x) and x[i] >= 0:
                i+=1
        if i==len(x):
            i = 0
            break
        elif n!= -1 and x[i]<0:
            break
    C = np.min(x)
    R = 1+ np.power(abs(i-n), C/x[n])
    return R
print(f"Теорема 4:{fourth(poli)}")


def fifth():
    R = fourth(poli)
    R1 = fourth(np.flip(poli))
    temp = []
    for i in range (len(poli)):
        if (len(poli)-1-i)%2==1:
            temp.append(-poli[i])
        else:
            temp.append((poli[i]))
    R2 = fourth(temp)
    R3 = fourth((np.flip(temp)))
    return (f"{1/R1}<=x+<={R} и {-R2}<=x-<={-1/R3}")
print(f"Теорема 5:{fifth()}")










