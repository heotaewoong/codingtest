T = int(input())

A = []
B = []
case = []
for i in range(T) :
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)
    case.append(a + b)

k = 0
for j in range(len(case)) :
    print(f"Case #{k + 1}: {A[k]} + {B[k]} = {case[k]}")
    k += 1