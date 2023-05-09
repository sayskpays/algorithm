# A,B,V=map(int, input().split())
# F = A - B
#
# cnt = 1
# while True:
#     cnt += 1
#     if (F* cnt) + A > V:
#         break
#
# print(cnt)
import math
import sys

input = sys.stdin.readline()
a,b,v = map(int,input.split())

day = math.ceil((v-a)/(a-b))+1
print(day)