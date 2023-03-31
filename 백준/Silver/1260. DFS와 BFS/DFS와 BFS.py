from collections import deque

n, m, v = map(int, input().split())
visited = [False] * (n + 1)
answer = []
visiteds = [False] * (n + 1)
answers = []
graph = [[] for _ in range(n + 1)]

for i in range(m):
    a, b = map(int, input().split())
    graph[a] += [b]
    graph[b] += [a]


# DFS
def dfs(v):
    visited[v] = True
    answer.append(v)
    for nv in sorted(graph[v]):
        if not visited[nv]:
            dfs(nv)
    return answer

# BFS
def bfs(v):

    Q = deque([v])
    visiteds[v] = True
    while Q:
        c = Q.popleft()
        answers.append(c)
        for j in sorted(graph[c]):
            if not visiteds[j]:
                Q.append(j)
                visiteds[j] = True
    return answers


print(*dfs(v))
print(*bfs(v))
