import string

Alp = list(string.ascii_uppercase)

Alp_number = {}
for i in range(len(Alp)) :
    Alp_number[Alp[i]] = i + 10

N, B = map(str, input().split())
B = int(B)

N_slicing = []
for i in range(len(N)) :
    N_slicing.append(N[i])

N = []
for j in range(len(N_slicing)) :
    if N_slicing[j] in Alp_number :
        N.append(Alp_number[N_slicing[j]])
    else :
        N.append(int(N_slicing[j]))

sum = 0
for k in range(len(N)) :
    sum += N[k] * (B ** (len(N) - k - 1))

print(sum)