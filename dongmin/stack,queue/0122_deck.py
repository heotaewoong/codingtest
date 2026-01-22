import sys
from collections import deque

input = sys.stdin.readline

n=int(input())
deck=deque()
for _ in range(n):
    k=input().split() #input에 띄어쓰기 있는데 split안하면 오류남 split하면 자동 리스트 반환
    #map(함수, 반복가능한것)
    #a = ["1", "2", "3"]
    # b = map(int, a)
    # print(list(b))   # [1, 2, 3]
    k=list(map(int,k))

    if k[0]== 1:
        deck.appendleft(k[1])
    elif k[0]== 2:
        deck.append(k[1])
    elif k[0]==3:
        print(deck.popleft() if deck else -1) #새로 배운 점
    elif k[0]==4:
        print(deck.pop() if deck else -1)
    elif k[0]==5:
        print(len(deck))    
    elif k[0]==6:
        print(0 if deck else 1)
    elif k[0]==7:
        print(deck[0] if deck else -1)
    elif k[0]==8:
        print(deck[len(deck)-1] if deck else -1)