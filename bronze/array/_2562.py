


data_list = []
for i in range(9):
    data_list.extend(map(int, input().splitlines()))


print(max(data_list), data_list.index(max(data_list))+1, sep="\n")

# #
# numbers = []
# for _ in range(9):
#     i = int(input())
#     numbers.extend(i)
#     print(numbers)
#
# print(max(numbers))
# print(numbers.index((max(numbers))+1)) # index 함수는 0부터 시작하기 떄문

