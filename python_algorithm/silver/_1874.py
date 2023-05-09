# 백준 실버 2 스택 수열

# 문제 이해가 안돼서 손도 못댐

# 해설 ...
import sys

n = int(sys.stdin.readline().strip())
stack = []
answer = []
flag = 0
cnt = 1

for _ in range(n):
    a = int(sys.stdin.readline().strip())
    while cnt <= a:
        stack.append(cnt)
        answer.append("+")
        cnt += 1

    if stack[-1] == a:
        stack.pop()
        answer.append("-")
    else:
        print("NO")
        flag = 1
        break

if flag == 0:
    for i in answer:
        print(i)


