#
# n = int(input())
# data_list = map(int,input().split())
# v = int(input())
# cnt = 0
#
# for i in data_list:
#     if i==v:
#         cnt +=1
#
# print(cnt)
#

n = int(input())
data_list = list(map(int, input().split()))
v = int(input())

print(data_list.count(v))
