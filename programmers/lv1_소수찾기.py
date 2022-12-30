
n = int(input())
sosu = [x for x in range(2, n+1)]
cnt = 0
for data in sosu:
    for i in range(2, int(data ** 0.5)+1):
        if data % i == 0:
            break
    else:
        cnt += 1



print(cnt)



