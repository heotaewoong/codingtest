M = int(input())
N = int(input())

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

prime_number = []
for num in range(M, N+1) :
    if is_prime(num):
        prime_number.append(num)

if prime_number:
    print(sum(prime_number))
    print(min(prime_number))
else:
    print(-1)