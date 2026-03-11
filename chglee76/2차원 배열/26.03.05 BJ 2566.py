max_value = -1
max_r = 1
max_c = 1

for i in range(1, 10) :
    row = list(map(int, input().split()))
    for j, v in enumerate(row, 1) :
        if v > max_value :
            max_value = v
            max_r, max_c = i, j

print(max_value)
print(max_r, max_c)