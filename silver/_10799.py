import sys

data = list(sys.stdin.readline().rstrip())
answer = 0
stack = []

for i in range(len(data)):
    if data[i] == '(':
        stack.append('(')
    else:
        if data[i-1] == '(':
            stack.pop()
            answer += len(stack)
        else:
            stack.pop()
            answer += 1

print(answer)