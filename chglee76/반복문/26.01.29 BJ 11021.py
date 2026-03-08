T = int(input())

case = []
for i in range(T) :
    A, B = map(int, input().split())
    case.append(A + B)

a = 0
for j in range(len(case)) :
    print(f"Case #{a+1}: {case[a]}")
    a += 1