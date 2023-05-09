# n = int(input())
# data_list = []
# new_list = []
# cnt = n
#
# for i in range(n):
#     inputValue = input()
#     data_list.append(inputValue)
#
# for data in data_list:
#     for i in range(len(data)-1):
#         if data[i] != data[i+1] or data[i] == data[i+1]:
#             new_list.append(data[i])
#         elif data[i] != data[i+1] and data[i] in new_list:
#             cnt -= 1
# print(new_list)
# print(cnt)
#

n = int(input())

group_word = 0
for _ in range(n):
    word = input()
    error = 0

    for i in range(len(word)-1): # 0부터 시작하기 때문에 n-1 을 해줘야 Index out of range 발생하지 않음
        if word[i] != word[i+1]:
            new_word = word[i+1:]
            if new_word.count(word[i]) > 0: # 남은 문자열에서 현재글자가 있었다면
                error += 1

    if error == 0:
        group_word += 1

print(group_word)