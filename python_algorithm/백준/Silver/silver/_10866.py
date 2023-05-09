import sys
from collections import deque

deque = deque()

for _ in range(int(sys.stdin.readline())):
    command = list(sys.stdin.readline().split())

    if command[0] == 'push_front':
        deque.append(command[1])
    elif command[0] == 'push_back':
        deque.appendleft(command[1])
    elif command[0] == 'pop_front':
        if deque:
            print(deque.pop())
        else:
            print(-1)
    elif command[0] == 'pop_back':
        if deque:
            print(deque.popleft())
        else:
            print(-1)
    elif command[0] == 'size':
        print(len(deque))
    elif command[0] == 'empty':
        if deque:
            print(0)
        else:
            print(1)
    elif command[0] == 'front':
        if deque:
            print(deque[-1])
        else:
            print(-1)
    else:
        if deque:
            print(deque[0])
        else:
            print(-1)
