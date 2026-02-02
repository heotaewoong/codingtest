'A%B' = set()

for i in range(10) :
    A = int(input())
    'A%B'.add(A % 42)

print(len('A%B'))