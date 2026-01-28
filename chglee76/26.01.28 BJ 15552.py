import sys

sys_input = sys.stdin.readline

T = int(sys_input())

output = []

for i in range(T) :
    a, b = map(int, sys_input().split())
    output.append(str(a + b))

sys.stdout.write("\n".join(output))