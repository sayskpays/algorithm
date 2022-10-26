
print(130%60)

h, m = map(int, input().split())
need_m = int(input())

if m + need_m % 60 == 0:
    h = m + need_m / 60
    m = 0
elif m + need_m > 60:
    h += round((m + need_m) / 60)
    if h>=24:
        h = round((m + need_m) / 60) - 1
    m = (m + need_m) % 60
else:
    m = m + need_m


print(h, m)


