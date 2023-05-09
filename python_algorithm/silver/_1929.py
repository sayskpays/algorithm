# import sys
#
# input = sys.stdin.readline()
# m,n = map(int,input.split())
#
# data_list = [x for x in range(m, n+1) if x%2 != 0 and x%3 != 0 and x%5 != 0]
#
# if m <= 2:
#     data_list.insert(0, 2)
#     data_list.insert(1, 3)
#     data_list.insert(2,5)
# elif 3 <= m < 4:
#     data_list.insert(0,3)
#     data_list.insert(1,5)
# elif m <= 5:
#     data_list.insert(0, 5)
#
# for data in data_list:
#     if data == 1:
#         continue
#     print(data)

m,n=map(int,input().split())

for i in range(m,n+1):
    if i==1:
        continue
    for j in range(2,int(i**0.5)+1):
        if i%j==0:
            break
    else:
        print(i)

