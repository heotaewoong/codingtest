word = input().strip()

Croatian_alphabet = ["dz=", "c=", "c-", "d-", "lj", "nj", "s=", "z="]

for i in Croatian_alphabet :
    word = word.replace(i, "*")

print(len(word))
