AperB = set()

for i in range(10) :
    A = int(input())
    AperB.add(A % 42)

print(len(AperB))