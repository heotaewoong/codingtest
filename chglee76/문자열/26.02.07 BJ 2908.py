A, B = input().split()
rev_A = int(A[::-1])
rev_B = int(B[::-1])

if rev_A > rev_B :
    print(rev_A)
else :
    print(rev_B)
