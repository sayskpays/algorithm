L=list(map(int,input().split()))
target = int(input())
lower = 0 # 리스트의 맨 처음 인덱스
upper = len(L) -1 # 리스트의 맨 끝 인덱스
idx = -1 # 원소가 발견되는 인덱스 위치

if target in L:

    while lower <= upper:
        middle = (lower + upper) // 2

        if L[middle] == target :
            idx = middle
            break
        elif L[middle] < target:
            lower = middle + 1
        else:
            upper = middle - 1

print(idx)



