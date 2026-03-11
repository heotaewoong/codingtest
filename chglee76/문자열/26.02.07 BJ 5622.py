word = input().strip()

dial = ["ABC", "DEF", "GHI",
        "JKL", "MNO", "PQRS",
        "TUV", "WXYZ"
        ]

time = 0

for i in word :
    for j, alp in enumerate(dial) :
        if i in alp :
            time += j + 3
            break

print(time)