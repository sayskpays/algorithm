
L = list(map(int,input().split()))
x = int(input())
answer = []

for i in range(len(L)):
    if L[i] == x:
        answer.append(i)

if x not in L:
    answer.append(-1)

print(answer)
