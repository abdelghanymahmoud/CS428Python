
# https://www.geeksforgeeks.org/graph-plotting-python-set-2/

import matplotlib.pyplot as plt

MaxRange = 100000
prime = list(range(0, MaxRange))

for i in range(2, MaxRange):
    prime[i] = True

prime[1] = False
for i in range(2, MaxRange):
    if prime[i]:
        for j in range(i * 2, MaxRange, i):
            prime[j] = False

vec = list()
for i in range(2, MaxRange):
    if prime[i]:
        # print(i)
        vec.append(i)

# x-coordinates of left sides of bars
number = range(10)
# heights of bars
value = []

cnt = 0
for i in range(10):
    if prime[i]:
        cnt = cnt + 1
    value.append(cnt)

# labels for bars
# tick_label = ['one', 'two', 'three', 'four', 'five']

# plotting a bar chart
plt.bar(number, value)

# naming the x-axis
plt.xlabel('x - axis')
# naming the y-axis
plt.ylabel('y - axis')
# plot title
plt.title('My bar chart!')

# function to show the plot
plt.show()