MaxRange = 100000
prime = list(range(0, MaxRange))

for i in range(2, MaxRange):
    prime[i] = True

for i in range(2, MaxRange):
    if prime[i]:
        for j in range(i * 2, MaxRange, i):
            prime[j] = False

vec = list()
for i in range(2, MaxRange):
    if prime[i]:
        # print(i)
        vec.append(i)

# for i in range(0, len(vec)):
#     print(vec[i])

x = int(input("enter x:"))
n = eval(input("enter n:"))

res = 0
for i in range(1, x):
    if i >= len(vec):
        break
    if vec[i] - vec[i - 1] == 2 * n and vec[i] < x:
        print(vec[i], vec[i - 1])
        res = res + 1

print(res)
