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
n = eval(input("enter n:"))
ind=0
cnt=0
while(n!=1 and vec[ind]<=n):
    while(n%vec[ind]==0):
        cnt+=1
        n//=vec[ind]
    ind+=1
print("n= ",n)
print("cnt= ",cnt)
if cnt%2==0:
    print(1)

else:
    print(-1)
