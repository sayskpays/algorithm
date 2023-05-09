
s = list(map(int,input().split()))
c = []

for i in range(len(s)):
    if s[i] % 2 != 0:
        s[i] -= 1
    c.extend(str(i)*(s[i]//2))

result = ''.join(map(str,c)) + '0' + ''.join(map(str,reversed(c)))

print(result)


