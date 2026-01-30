N=int(input())
hash=list(map(int,input().split()))

m=int(input())
lst=list(map(int,input().split()))

count={}
for x in hash:
    if x in count:
        count[x] +=1
    else:
        count[x]=1

ans=[]
for q in lst:
    ans.append(count.get(q,0))

print(*ans)