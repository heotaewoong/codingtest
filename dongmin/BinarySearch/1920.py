import sys
input = sys.stdin.readline

N=int(input())
hash=set(map(int,input().split()))
n=int(input())
question=list(map(int,input().split()))

for i in question:
    print(1 if i in hash else 0)

# 이분탐색버전
