n, k = map(int, input().split())
wons = []
cnt = 0

for _ in range(n):
    wons.append(int(input()))

wons = [i for i in wons if i <= k]
wons.sort(reverse=True)

for won in wons:
    cnt += (k//won)
    k %= won

print(cnt)