import sys

n, m = map(int, sys.stdin.readline().split())

a = [list(map(int, sys.stdin.readline().split())) for _ in range(n)] # 문자열 n개를 받아 int 요소로 바꾸고 list로 변환하여 a에 저장 (리스트) 첫번째 3x3 배열
b = [list(map(int, sys.stdin.readline().split())) for _ in range(n)] # 두번쨰 3x3 배열

for i in range(n):
    for j in range(m):
        a[i][j] += b[i][j]

for i in a:
    print(*i)
