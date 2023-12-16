import numpy as np
import math

x = [2, 3, 4, 5]
f = [7, 5, 8, 7]
f_x0_x1 = ((f[1] - f[0]) / (x[1] - x[0]))
f_x1_x2 = ((f[2] - f[1]) / (x[2] - x[1]))
f_x2_x3 = ((f[3] - f[2]) / (x[3] - x[2]))
f_x0_x1_x2 = ((f_x1_x2 - f_x0_x1) / (x[2] - x[0]))
f_x1_x2_x3 = ((f_x2_x3 - f_x1_x2) / (x[3] - x[1]))
f_x0_x1_x2_x3 = ((f_x1_x2_x3 - f_x0_x1_x2) / (x[3] - x[0]))
N3_x = np.poly1d([x[0], x[1], x[2]], True)*f_x0_x1_x2_x3 + np.poly1d([x[0], x[1]],True)*f_x0_x1_x2 + np.poly1d([x[0]], True)*f_x0_x1 + f[0]
print(f"Многочлен Ньютона 3-ей степени:\n {N3_x}")

h = x[1] - x[0]
q = np.poly1d([1/h, -x[0]/h])
f0_1 = f[1] - f[0]
f1_1 = f[2] - f[1]
f2_1 = f[3] - f[2]
f0_2 = f1_1 - f0_1
f1_2 = f2_1 - f1_1
f0_3 = f1_2 - f0_2
pol1 = np.poly1d([1/h, -x[0]/h])
pol2 = pol1 * np.poly1d([1/h, -x[0]/h - 1])
pol3 = (pol2 * np.poly1d([1/h, -x[0]/h - 2]))
N3_1_x = f[0] + f0_1*pol1 + f0_2/2*pol2 + f0_3/6*pol3
print(f"Первый интерполяционный многочлен Ньютона:\n {N3_1_x}")

q_hat = np.poly1d([1/h, -x[3]/h])
pol1_hat = np.poly1d([1/h, -x[3]/h])
pol2_hat = pol1_hat * np.poly1d([1/h, -x[3]/h + 1])
pol3_hat = (pol2_hat * np.poly1d([1/h, -x[3]/h + 2]))
N3_2_x = f[3] + f2_1*pol1_hat + f1_2/2*pol2_hat + f0_3/6*pol3_hat
print(f"Первый интерполяционный многочлен Ньютона:\n {N3_2_x}")