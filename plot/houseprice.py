import matplotlib as mpl
from matplotlib import pyplot as plt
import numpy as np

x = np.arange(25, 45)
y1 = 200*1.1**(x-25)
y2 = 40*(x-25)
y3 = y1-y2


x0 = 7.7765118542516927
y0 = 200*1.1**x0
c = y0 - 40*x0

y4 = 40*(x-25) + c

p1 = (x0+25, y0)
p2 = (25, c)
p3 = (x0+25, c)

plt.plot(x, y4, '--', label='y=40*x+%.1f'%c)
plt.plot(x, [c]*len(x), '--', label='y=%.1f'%c)
plt.plot(x, y1, label='y1=200*1.1^x')
plt.plot(x, y2, label='y2=40*x')
plt.plot(x, y3, label='y3=y1-y2')
plt.plot([p1[0], p2[0], p3[0]], [p1[1], p2[1], p2[1]], 'o')
plt.grid(True)
plt.legend(loc=0)

def s(p):
    return '(%.1f, %.1f)' % p
plt.annotate(s(p1), xy=p1, xytext=(p1[0]-2,600), arrowprops=dict(arrowstyle='->'))
plt.annotate(s(p2), xy=p2, xytext=(p2[0]+1,600), arrowprops=dict(arrowstyle='->'))
plt.show()
