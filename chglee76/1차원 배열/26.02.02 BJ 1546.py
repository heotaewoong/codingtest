N = int(input())
score = list(map(int, input().split()))

M = max(score)
sum_score = 0
for _score in score :
    sum_score += _score / M * 100

print(sum_score/N)