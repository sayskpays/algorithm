# from math import trunc
#
# h, m = map(int, input().split())
# need_m = int(input())
#
# if m + need_m % 60 == 0:
#     h += trunc((m + need_m) / 60)
#     m = 0
# elif m + need_m > 60:
#     h += trunc((m + need_m) / 60)
#     if h>=24:
#         h -= 24
#     m = (m + need_m) % 60
# else:
#     m = m + need_m
#
# print(h, m)

# 해설


A, B = map(int, input().split())
C = int(input())

A += C // 60
B += C % 60

if B >= 60:
    A += 1
    B -= 60

if A >= 24:
    A -= 24

print('%d %d' % (A, B))



