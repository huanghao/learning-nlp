import matplotlib as mpl
from matplotlib import pyplot as plt
import numpy as np


x = np.arange(-0.5, 1.5, .01)
plt.plot(x, x**2, '--', x, np.sqrt(x), range(3), range(3), ':o')
plt.grid(True)
plt.xlabel('Here is the X axis')
plt.ylabel('This is the Y axis')
plt.title('Title of the demo')
plt.legend(['y=x^2', 'y=x^.5', 'y=x'], 0)
plt.axis([-1, 2.5, -1, 2.5])
plt.xticks([-.5, 0, 1, 1.5, 2])
plt.yticks([-.5, 0, 1, 1.5, 2])
plt.annotate('circle\nmarker', xy=(1,1), xytext=(1.2, .6), arrowprops=dict(facecolor='black',shrink=.1))
plt.annotate('this is called legend', xy=(-.1,2), xytext=(.1,1.5), arrowprops=dict(arrowstyle='fancy'))
plt.annotate('these are grid', xy=(1.5,-.75), xytext=(.5,-.5), arrowprops=dict(arrowstyle='->',connectionstyle='arc3,rad=.2'))
plt.annotate('these are grid', xy=(1.75,-.5), xytext=(.5,-.5), arrowprops=dict(arrowstyle='->',connectionstyle='arc3,rad=-.2'))
plt.annotate('x/y ticks', xy=(-.5,-1), xytext=(-.4,-.3), arrowprops=dict(arrowstyle='->'))
plt.annotate('x/y ticks', xy=(-1,-.5), xytext=(-.4,-.3), arrowprops=dict(arrowstyle='->'))
plt.annotate('x/y ticks', xy=(-1,0), xytext=(-.4,-.3), arrowprops=dict(arrowstyle='->'))
plt.annotate('x/y ticks', xy=(0,-1), xytext=(-.4,-.3), arrowprops=dict(arrowstyle='->'))
plt.show()
