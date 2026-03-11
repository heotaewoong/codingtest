number = int(input())

A = []
for i in range(number) :
    x, y = map(int, input().split())
    for j in range(x, x+10) :
        for k in range(y, y+10) :
            A.append((j, k))

print(len(set(A)))