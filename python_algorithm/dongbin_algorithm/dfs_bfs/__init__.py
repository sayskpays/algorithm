import sys

n = int(sys.stdin.readline().rstrip())
k = int(sys.stdin.readline().rstrip())
graph = [[] for i in range(n + 1)]
visited = [False] * (n + 1)

for _ in range(k):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    graph[a] += [b]
    graph[b] += [a]


def dfs(v):
    visited[v] = True  # 방문 등록
    for nx in graph[v]:
        if visited[nx] == False:
            dfs(nx)
dfs(1)
print(sum(visited) - 1)
