n=int(input())

for _ in range(n):
    lst=list(input())
    m=[]
    flag=1
    for k in lst:
        if k=='(':
            m.append('(')
        elif m:
            if k == ")":
                m.pop()
        else:
            flag=0
    if m:
        print('NO')
    elif flag==0:
        print('NO')
    else:
        print('YES')
    
    
# ##import sys
# input = sys.stdin.readline

# n = int(input())
# for _ in range(n):
#     s = input().strip()
#     cnt = 0
#     ok = True

#     for ch in s:
#         if ch == '(':
#             cnt += 1
#         else:  # ')'
#             cnt -= 1
#             if cnt < 0:      # 닫는 괄호가 먼저 나오면 즉시 실패
#                 ok = False
#                 break

#     print("YES" if ok and cnt == 0 else "NO")
    
    


