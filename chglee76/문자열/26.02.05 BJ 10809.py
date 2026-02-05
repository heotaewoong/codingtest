S = input()

print(*[S.find(chr(i)) for i in range(ord('a'), ord('z') + 1)])
