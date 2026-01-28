import sys
input=sys.stdin.readline

N=int(input())
A=list(map(int,input().split()))
A.sort()

M=int(input())
Q=list(map(int,input().split()))

def exists(arr,x):
    lo,hi = 0, len(arr)-1
    while lo<=hi:
        mid = (lo+hi)//2
        if arr[mid] == x:
            return True
        elif arr[mid] < x:
            lo = mid +1
        else:
            hi = mid-1
    return False

out=[]
for x in Q:
    out.append('1' if exists(A,x) else '0')

sys.stdout.write('\n'.join(out))
#lo는 점점 올라가고 hi는 점점 내려와서 교차가 되면 False