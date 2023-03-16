n = input()
arr = []
start = n[0]
for i in n:
    if start == i:
        continue
    else:
        start = i
        arr.append(1)

print((arr.count(1)+1) // 2)

