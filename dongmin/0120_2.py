# 10845 queue

import sys
input = sys.stdin.readline

queuelist=[]
def push(n):
    queuelist.append(n)
def pop():
    if len(queuelist)==0:
        return -1
    else:
        return queuelist.pop(0)
def size():
    return len(queuelist)
def empty():
    if len(queuelist)==0:
        return 1
    else:
        return 0 
def front():
    if len(queuelist)==0:
        return -1
    else:
        return queuelist[0]
def back():
    if len(queuelist)==0:
        return -1
    else:
        return queuelist[len(queuelist)-1]    




n=int(input())
for _ in range(n):
    cmd=input().split()
    if cmd[0]=='push':
        push(int(cmd[1]))
    elif cmd[0]=='size':
        print(size())
    elif cmd[0]=='empty':
        print(empty())
    elif cmd[0]=='front':
        print(front())
    elif cmd[0]=='back':
        print(back())
    elif cmd[0]=='pop':
        print(pop())




#터미널에서는 \n으로 입력된 것은 뭉터기로 입력되는 것이 아니라 
#한 줄씩 입력되는 것이다.
#따라서 5\n10\n20\n30\n40\n50\n 이렇게 입력하면 
#첫 번째 줄에 5가 입력되고 두 번째 줄에 10이 입력되는 것이다.
#따라서 n=int(input())을 하면 첫 번째 줄에 입력된 5가 n에 저장되는 것이다.
#그리고 print(n)을 하면 n에 저장된 5가 출력되는 것이다.
#이와 같이 \n은 터미널에서 줄바꿈의 의미이지 입력값의 일부가 아니다.
#그래서 n = int(input())
#for _ in range(n):
#    cmd = input().split() 한줄씩 입력을 받아서 cmd에서 처리되는것