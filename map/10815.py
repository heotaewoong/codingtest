N=int(input())
hash=set(map(int,input().split()))

m=int(input())
lst=list(map(int,input().split()))
ans=[]
for i in lst:
    if i in hash:
        ans.append(1)
    else:
        ans.append(0)

print(*ans)

