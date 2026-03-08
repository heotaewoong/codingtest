N, X = map(int, input().split())

A = []
A[:N] = map(int, input().split())

number = []
for i in A :
    if i < X :
        number.append(i)

print(*number)
