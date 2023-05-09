from collections import deque

k = int(input())

for _ in range(k):
    cnt = 0
    n, m = map(int, input().split())
    data = list(map(int, input().split()))
    Q = deque(data)

    if len(Q) == 1:
        print(1)
        continue

    while len(Q) > 0:
        if Q[0] == max(Q):
            Q.popleft()
            if Q.index(Q[m]) == len(Q)-1:
                m = len(Q) -1
            cnt += 1
            if Q[m] == max(Q):
                print(cnt)
                break
        else:
            Q.append(Q.popleft())
            m -= 1


