T = int(input())

A = []
B = []

for i in range(T) :
    a, b = map(int,input().split())
    A.append(a)
    B.append(b)

k = 0
for j in range(len(A)) :
    print(A[k] + B[k])
    k += 1