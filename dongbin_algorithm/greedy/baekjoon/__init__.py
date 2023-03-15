n, l = map(int, input().split())

diff = 0.5
spot = sorted(list(map(int, input().split())))
a = []
b = []
count = 1
temp = 0
for i in spot:
    a += [i - diff]
    b += [i + diff]

for j in range(1, n+1):
    temp += b[j] - a[j]
    if temp >= l:
        count += 1
        temp = 0
    else:
        continue

print(count if temp == 0 else count+1)
