n, m = map(int, input().split())
answer = []
for _ in range(n):
    data = list(map(int, input().split()))
    data.sort()
    answer.append(data[0])

print(answer[-1])