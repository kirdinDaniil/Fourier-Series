import matplotlib.pyplot as plt
import math

xi = -4*3.14

coef = -1

x = []

y = []

maxn = int(input())

while xi < 4*3.14:
    yi = 0
    yi += ((math.pi+4)/(2*math.pi))*math.sin(xi)
    if round(xi, 2) == (2*coef-1)*3.14:
        plt.plot(x, y)
        x.clear()
        y.clear()
        x.append(xi)
        y.append(0)
        plt.plot(x, y, color='green', marker='o', markersize=7)
        x.clear()
        y.clear()
        coef += 1
        xi += 0.1
        continue

    for n in range(2, maxn):
        #yi -= 2*(math.cos(math.pi*n/2) + math.pow(-1, n)*(math.pi*math.pow(n, 2)-1))/(math.pow(math.pi,2)*n*(math.pow(n,2)-1))*math.sin(xi*n)
        yi += ((-2*n*math.cos(math.pi * n / 2)) / (
                    math.pi *(math.pow(n, 2) - 1)) + (2*math.cos(math.pi * n / 2) - 2*math.pow(-1, n))/(math.pi*n)) * math.sin(xi * n)

    x.append(xi)
    y.append(yi)
    xi += 0.01

plt.plot(x, y)
plt.grid()
plt.xlabel('t') #Подпись для оси х
plt.ylabel('S(t)') #Подпись для оси y
plt.show()
