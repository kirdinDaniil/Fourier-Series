import matplotlib.pyplot as plt
import math

xi = -4*3.14

coef = -4

x = []

y = []

maxn = int(input())

while xi < 4*3.14:
    yi = (2+math.pi)/(2*math.pi)
    yi += (-1/math.pi)*math.cos(xi)

    for n in range(2, maxn):
        yi += (2*(math.sin(n*math.pi/2) - n))/(math.pi*n*(n*n-1))*math.cos(xi*n)

    x.append(xi)
    y.append(yi)
    xi += 0.01

plt.plot(x, y)
plt.grid()
plt.xlabel('t') #Подпись для оси х
plt.ylabel('S(t)') #Подпись для оси y
plt.show()
