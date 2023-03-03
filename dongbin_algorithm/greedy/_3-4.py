n, k = map(int, input().split())
cnt = n % k
n = n - cnt

while True:

    if n%k == 0:
        n //= k
        cnt += 1
    else:
        n -= 1
        cnt += 1
    if n == 1:
        break
print(cnt)