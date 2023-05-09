
# n = input().lower()
# alpha = [i for i in range(ord('a'), ord('z')+1)]
# data_list = []
#
# for j in alpha:
#     data_list.append(n.find(chr(j)))
#
# print(data_list)

word = input().lower()
word_list = list(set(word))
cnt = []


for i in word_list:
    count = word.count(i)
    cnt.append(count)

if cnt.count(max(cnt)) >= 2:
    print("?")
else:
    print(word_list[(cnt.index(max(cnt)))].upper())

print(cnt.index(max(cnt)))



