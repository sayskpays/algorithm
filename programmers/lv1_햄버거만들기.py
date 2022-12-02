ingredient = list(map(int, input().split()))
s = []
cnt = 0

for i in ingredient:
    s.append(i)
    if s[-4:] == [1,2,3,1]:
        cnt += 1
        del s[-4:]

print(cnt)