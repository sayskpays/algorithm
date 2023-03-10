# n = int(input())
#
# result = sorted([int(input()) for _ in range(n)], reverse=True)
# print(*result)

n = int(input())

result = []

for _ in range(n):
    input_data = list(map(str, input().split()))
    result.append(input_data)

result = sorted(result, key=lambda a:a[1])

for a in result:
    print(a[0], end=' ')
