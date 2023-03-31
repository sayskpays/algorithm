n = int(input())
data = list(map(int, input().split()))

data.sort()
cnt = 0
for i in range(len(data)):
    cnt += (data[i] * n)
    n -= 1
print(cnt)





