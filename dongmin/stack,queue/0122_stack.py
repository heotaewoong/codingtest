lst=[]
n=int(input())

for i in range(n):
    k=int(input())
    if k != 0:
        lst.append(k)
    elif k ==0:
        lst.pop()

h=0
for j in lst:
    h=h+j
print(h)