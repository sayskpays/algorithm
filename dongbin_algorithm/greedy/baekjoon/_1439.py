n = input()
arr = []
start = n[0]
for i in n:
    if start == i:
        continue
    else:
        start = i
        arr.append(1)

if len(arr) == 1:
    print(1)
elif arr is []:
    print(0)
else:
    print(len(arr) // 2)
