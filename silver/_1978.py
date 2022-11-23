#
# n= int(input())
#
# a = list(map(int,input().split()))
# cnt = 0
#
# for i in a:
#     if i == 1:
#         continue
#     elif i == 3:
#         cnt += 1
#     elif i == 2:
#         cnt += 1
#     elif i%2 != 0 and i%3 != 0:
#         cnt += 1
#
# print(cnt)

n = int(input())
data = list(map(int,input().split()))
cnt = 0

for x in data:
    for i in range(2, x+1):
        if x%i == 0:
            if x == i:
                cnt += 1
            break
print(cnt)

