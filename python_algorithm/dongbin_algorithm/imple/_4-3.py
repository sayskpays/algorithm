n = list(input())
x = ord(n[0]) - 96
y = int(n[1])
x_cal = [2, -2, 1, -1, 1, -1, -2, 2]
y_cal = [1, 1, 2, 2, -2, -2, -1, -1]

cnt = 0

for i in range(len(x_cal)):
    xy = x + x_cal[i]
    yx = y + y_cal[i]

    if xy < 1 or xy > 8 or yx < 1 or yx > 8:
        continue
    else:
        cnt += 1

print(cnt)



