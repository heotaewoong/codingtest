#2941
s=input()

for i in ('c=','c-','dz=','d-','lj','nj','s=','z='):
    s=s.replace(i,'*')
print(len(s))

#replace함수사용법과 replace를 반환해줘야지