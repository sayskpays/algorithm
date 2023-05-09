t = int(input())
time = [300, 60, 10]
answer = []
count = 0

for i in range(len(time)):
    if t // time[i] != 0:
        answer.append(t // time[i])
        t %= time[i]
        count += t // time[i]
    else:
        answer.append(t // time[i])
        continue

print(*answer) if t == 0 else print(-1)
