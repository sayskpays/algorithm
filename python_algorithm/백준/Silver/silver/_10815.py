# 이분 탐색이 아닌 풀이 방법

N = int(input())
A = set(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))

for num in B:
    print(1, end=' ') if num in A else print(0, end=' ')