
n = int(input())  # 컴퓨터 개수
v = int(input())  # 연결선 개수
# 1부터 사용하기 위해서 range(n + 1)
graph = [[] for i in range(n + 1)]  # 그래프 초기화
visited = [0] * (n + 1)  # 방문한 컴퓨터인지 표시
for _ in range(v):  # 그래프 생성
    a, b = map(int, input().split())
    graph[a] += [b]  # a에 b 연결
    graph[b] += [a]  # b에 a 연결 -> 양방향

def dfs(v):
    visited[v]=1
    for nx in graph[v]:
        if visited[nx]==0: # 방문되지 않은 컴퓨터인지 확인
            dfs(nx) # 방문되지 않았다면 컴퓨터 방문
dfs(1)
print(sum(visited)-1) # -1을 한 이유는 1번 컴퓨터를 제회하고, 1번 컴퓨터와 연결된
# 컴퓨터 개수를 출력해야 하기 때문이다.







