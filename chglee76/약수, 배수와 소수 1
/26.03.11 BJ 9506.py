while True :
    n = int(input())
    
    if n == -1 : break
    
    factor = []
    for i in range(1, n) :
        if n % i == 0 :
            factor.append(i)
    
    if sum(factor) == n :
        print(f"{n} = {' + '.join(map(str, factor))}")
    else :
        print(f"{n} is NOT perfect.")