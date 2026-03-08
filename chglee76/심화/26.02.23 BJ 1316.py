n = int(input())
A = 0

for _ in range(n):
    word = input().strip()
    if list(word) == sorted(word, key=word.find):
        A += 1

print(A)