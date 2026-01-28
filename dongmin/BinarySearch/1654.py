import sys
input = sys.stdin.readline

N,M=map(int,input().split())
lst=[]
for _ in range(N):
    a=int(input())
    lst.append(a)

lo, hi =1 ,max(lst)
ans=0 

while lo <= hi:
    mid=(lo+hi)//2
    count=sum(x//mid for x in lst)
    # 길이로 나눈다음에 조각 갯수의 합이 M보다 작으면 hi=mid
    if count >= M: #만들 수 있으면
        lo=mid+1 #정답 후보
        ans=mid # 더 길게 시도
    else:
        hi=mid-1 #너무 김 줄이기

print(ans)