import sys
import math
input = sys.stdin.readline

N=list(map(int,input().split()))
HIGHT=list(map(int,input().split()))
k=N[1]





top=(sum(HIGHT)-k)/N[0]
print(math.floor(top))