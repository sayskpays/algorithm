# while True:
#     w, h = map(int, input().split())
#     if w == 0 and h == 0:
#         break
#     graph = [[] for i in range(w * h + 1)]
#     visited = [0] * (w * h + 1)
#     row = [0]
#     for _ in range(h):
#         map_data = list(map(int, input().split()))
#         row.extend(map_data)
#
#     for i in range(len(row)):
#         if i == 0:
#             continue
#         graph[i] += [row[i] * i]


# 해설

import sys
read = sys.stdin.readline()
sys.setrecursionlimit(10**6)

def dfs(x, y):
    dx = [1, 1, -1, -1, 1, -1, 0, 0]
    dy = [0, 1, 0, 1, -1, -1, 1, -1]

    field[x][y] = 0
    for i in range(len(dx)):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < h and 0 <= ny < w and field[nx][ny] == 1:
            dfs(nx, ny)

while True:
    w, h = map(int, read.split())
    if w == 0 and h == 0:
        break
    field = []
    count = 0
    for _ in range(h):
        field.append(list(map(int, read.split())))
    for i in range(h):
        for j in range(w):
            if field[i][j] == 1:
                dfs(i,j)
                count += 1
    print(count)
