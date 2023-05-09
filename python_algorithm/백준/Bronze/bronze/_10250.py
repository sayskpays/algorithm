import math
import sys

t = int(input())

for _ in range(t):
    h,v,n=map(int,input().split())
    floor = h if n%h == 0 else n%h
    room = math.ceil(n/h)


    print(f'{floor}{room:0>2}')
