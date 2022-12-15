
arr = list(map(int, input().split()))
new_arr = list()
new_arr.append(arr[0])

for i in arr:
    if i not in new_arr:
        new_arr.append(i)
    else:
        if new_arr[-1] != i:
            new_arr.append(i)

print(new_arr)
