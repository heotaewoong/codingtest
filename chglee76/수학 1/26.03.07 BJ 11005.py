import string

Alp = list(string.ascii_uppercase)

number_Alp = {}
for i in range(len(Alp)) :
    number_Alp[i + 10] = Alp[i]

N, B = map(int, input().split())

result = []

while N > 0 :
    remain = N % B
    
    if remain >= 10 :
        result.append(number_Alp[remain])
    else :
        result.append(str(remain))
    
    N = N // B

result.reverse()

for i in range(len(result)) :
    print(result[i], end="")