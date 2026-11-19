###
# Draws the graph of y = sin(x) for angle 0-360 degrees
#
import matplotlib.pyplot as plt
import math

x = []
y = []

for n in range(0, 361):
    x = x + [n]
    y = y + [math.sin(math.radians(n))]

plt.plot(x, y)
plt.show()