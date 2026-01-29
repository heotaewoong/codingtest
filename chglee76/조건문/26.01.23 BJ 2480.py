i, j, k = map(int,input().split())
dice = [i, j, k]

biggest_number = max(dice)
same_number = [number for number in set(dice) if dice.count(number) > 1]
same_number_count = len(set(dice))

if same_number_count == 1:
    print(10000 + same_number[0] * 1000)
elif same_number_count == 2:
    print(1000 + same_number[0] * 100)
else :
    print(biggest_number * 100)