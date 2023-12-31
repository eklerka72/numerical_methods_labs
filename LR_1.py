import math
funk = input()
def f(x):
    global funk
    return eval(funk)

def dih (x0, x1, eps, max_iter = 1e5):
    i = 0
    while (abs(x1-x0) > eps) and (i < max_iter):
        x2 = (x1+x0)/2
        if f(x2)*f(x1) < 0:
            x0 = x2
        elif f(x2)*f(x0) < 0:
            x1 = x2
        elif f(x2) == 0:
            return x2
        i += 1
    return None


def simple_iteration(x0, eps, max_iter, a):
    for i in range(max_iter):
        x1 = 1/2*(x0 + a/x0)
        if abs(x0-x1)<eps:
            return x1
        else:
            x0=x1
    return x0

print(dih(0, 10, 0.0))
print(f"Корень квадратный из {30}")
print(simple_iteration(5, 0.00001, 20, 30))