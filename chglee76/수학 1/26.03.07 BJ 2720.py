coin = [25, 10, 5, 1]

T = int(input())

for i in range(T) :
    C = int(input())
    
    result = []
    
    for j in range(len(coin)) :
        result.append(C // coin[j])
        C = C % coin[j]
    
    for k in range(len(result)) :
        print(result[k], end=" ")
    print()