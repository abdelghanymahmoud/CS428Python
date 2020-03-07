import matplotlib.pyplot as plt
from random import random

MaxX = 1000
# x-axis values
x = []
# y-axis values
y = []

def path():
    I = 0
    J = 0;
    while I < MaxX:
        if random() > 0.5:
            J = J - 1
        else:
            J = J + 1
        I = I + 1
        x.append(I)
        y.append(J)

ave = 0
for i in range(100):
    x = []
    y = []
    path()
    # plotting points as a scatter plot
    plt.scatter(x, y, label="stars", color="blue", marker="*", s=5)
    ave = ave + abs(y[MaxX - 1])
    print(i+1, "distance=",abs(y[MaxX - 1]))

print("ave=", ave/100)
# x-axis label
plt.xlabel('x - axis')
# frequency label
plt.ylabel('y - axis')
# plot title
plt.title('My scatter plot!')
# showing legend
plt.legend()

# function to show the plot
plt.show()