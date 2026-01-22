import sys
from collections import deque

input = sys.stdin.readline

N=int(input())
moves = list(map(int,input().split()))

dq=deque((i+1,moves[i]) for i in range(N))
ans=[]

while deque:
    idx,k = dq.popleft()
    ans.append(idx)

    if deque:
        if k >0 :
            deque.rotate(-(k-1))
        else: dq.rotate(-k)

Print(*ans) #리스트 안의 값들이 공백으로 나뉘어서 출력됨