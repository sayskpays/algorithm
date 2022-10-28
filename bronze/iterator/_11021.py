
T = int(input())
a= []

for i in range(1,T+1):
    A, B = map(int, input().split())
    a.append("Case #{}: {}".format(i, A+B))

for item in a:
    print(item)

