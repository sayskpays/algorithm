# (king, queen, look, bishop, night, phone) = (1, 1, 2, 2, 2, 8)
# chese_data = (king, queen, look, bishop, night, phone)
#
# input_list = list(map(int, input().split(" ")))
# new_list = []
#
#
# i = 0
# while i < len(chese_data):
#     new_list.append(chese_data[i] - input_list[i])
#     i += 1
#
# for item in new_list:

#     print(item, end=" ")

chess = [1,1,2,2,2,8]

hong = list(map(int, input().split()))

for i in range(6):
    print(chess[i] - hong[i], end=' ')


