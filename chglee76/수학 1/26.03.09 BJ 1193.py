import math

X = int(input())

def triangular_inverse(X) :
    n = (math.sqrt(8*X + 1) - 1) / 2

    a = math.floor(n)

    if a * (a + 1) // 2 >= X :
        a -= 1

    b = a + 1

    return a, b

A, B = triangular_inverse(X)

def Range(A, B) :
    R_A = A * (A + 1) // 2 + 1
    R_B = B * (B + 1) // 2

    return R_A, R_B

R_A, R_B = Range(A, B)

location = int(X - R_A)

if B % 2 == 0 :
    fraction = f"{1 + location}/{B - location}"
else :
    fraction = f"{B - location}/{1 + location}"

print(fraction)