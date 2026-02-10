from collections import Counter

alp = input().upper()

count_alp = Counter(alp)

Max_alp = max(count_alp.values())
print('?' if list(count_alp.values()).count(Max_alp) > 1 else max(count_alp, key=count_alp.get))