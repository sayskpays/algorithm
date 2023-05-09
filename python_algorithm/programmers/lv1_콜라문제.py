
a = int(input())
b = int(input())
n = int(input())
cnt = 0
noa = 0
hap = 0

while True:
    if n >= a:
        cnt = n//a
        noa = n%a
        n = cnt + noa
        hap += cnt
    else:
        break

print(hap)
