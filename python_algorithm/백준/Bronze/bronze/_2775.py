
n = int(input())
cnt = 0
for _ in range(n):
    k = int(input()) # 층
    n = int(input()) # 호
    f0 = [x for x in range(1, n+1)] # 0층 리스트

    for k in range(k): # 층 수 만큼 반복
        for i in range(1, n): # 1 ~ n-1 까지 인덱스로 사용
            f0[i] += f0[i-1] # 층별 각 호실의 사람 수를 변경

    print(f0[-1])

