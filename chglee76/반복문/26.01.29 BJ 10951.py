case = []
while True : 
    try :
        a, b = map(int, input().split())
        case.append(a + b)
    except :
        break

a = 0
for i in range(len(case)) :
    print(case[a])
    a += 1
