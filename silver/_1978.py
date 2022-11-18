
n= int(input())

a = list(map(int,input().split()))
cnt = 0

for i in a:
    if i == 1:
        continue
    elif i == 3:
        cnt += 1
    elif i == 2:
        cnt += 1
    elif i%2 != 0 and i%3 != 0:
        cnt += 1

print(cnt)




