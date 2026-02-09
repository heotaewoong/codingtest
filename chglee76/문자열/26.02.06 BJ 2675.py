S = int(input().strip())

for i in range(S) :
    R, P = input().split()
    R = int(R)
    print(''.join(a * R for a in P))