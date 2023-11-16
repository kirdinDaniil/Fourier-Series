import matplotlib.pyplot as plt
import math

xi = -3*3.14

coef = -3

x = []

y = []

maxn = int(input())

while xi < 3*3.14:
    yi = (2+math.pi)/(2*math.pi)
    if round(xi, 2) == coef*3.14:
        plt.plot(x, y)
        x.clear()
        y.clear()
        x.append(xi)
        y.append(1/2)
        plt.plot(x, y, color='green', marker='o', markersize=7)
        x.clear()
        y.clear()
        coef += 1
        xi += 0.1
        continue
    for n in range(1, maxn):
        yi += (-2*math.cos(2*n*xi))/(4*math.pi*n*n-math.pi)+((-4*n*n-math.pow(-1,n)+1)*math.sin(2*n*xi))/(4*math.pi*n*n*n-math.pi*n)
    x.append(xi)
    y.append(yi)
    xi += 0.01

plt.plot(x, y)
plt.grid()
plt.xlabel('t') #Подпись для оси х
plt.ylabel('S(t)') #Подпись для оси y
plt.show()
