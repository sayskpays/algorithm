n, m, k = map(int, input().split())

data = list(map(int, input().split()))
data.sort()

count = data[-1] * (m - (m // k)) + (data[-2] * (m // k))
print(count)
