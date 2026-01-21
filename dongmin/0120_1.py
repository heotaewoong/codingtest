#stack 10828
intlist=[]
def push(n):
    intlist.append(n)

def pop():
    if len(intlist)==0:
        return -1
    else:
        return intlist.pop()

def size():
    return len(intlist)

def empty():
    if len(intlist)==0:
        return 1
    else:
        return 0   
def top():
    if len(intlist)==0:
        return -1
    else:
        return intlist[-1]
import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    cmd = input().split()

    if cmd[0] == "push":
        push(int(cmd[1]))
    elif cmd[0] == "pop":
        print(pop())
    elif cmd[0] == "size":
        print(size())
    elif cmd[0] == "empty":
        print(empty())
    elif cmd[0] == "top":
        print(top())

#return은 값을 반환하는 것이고 print는 값을 출력하는 것이다. 
#백준에서는 값을 출력해야하기에 print를 사용해야 한다.
# n=int(input()) 하면 input값을 받은 뒤에 int형으로 변환한 값을 n에 저장한다.
# sys.stdin.readline은 input()보다 속도가 빠르다.