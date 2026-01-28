N, A, B = map(int, input().split())

Bus_time = A
Subway_time = B
Subway_missing = B - N

if Subway_missing < 0 :
    print("Bus")
elif Subway_time == Bus_time :
    print("Anything")
elif Subway_time < Bus_time :
    print("Subway")
else : print("Bus")