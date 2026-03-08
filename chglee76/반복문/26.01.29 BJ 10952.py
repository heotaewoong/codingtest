
case = []
i = True


while True :
    a, b = map(int, input().split())
    if a == 0 and b == 0 :
        break
    case.append(a + b)

a = 0
for i in range(len(case)) :
    print(case[a])
    a += 1