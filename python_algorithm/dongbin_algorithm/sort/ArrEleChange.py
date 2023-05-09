
n, k = map(int, input().split())

a = sorted(list(map(int, input().split())))
b = sorted(list(map(int, input().split())), reverse=True)

for i in range(k):
    if a[i] < b[i]:
        a[i] = b[i]
    else:
        break

# cnt = 0
# c = -1
#
# for i in range(n):
#     if a[i] < b[c]:
#         a[i] = b[c]
#     c -= 1
#     cnt += 1
#     if cnt >= k:
#         break

print(sum(a))
