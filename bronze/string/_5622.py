# dic_data = {
#     '2': ['A','B','C'],
#     '3': ['D','E','F'],
#     '4': ['G','H','I'],
#     '5': ['J','K','L'],
#     '6': ['M','N','O'],
#     '7': ['P','Q','R','S'],
#     '8': ['T','U','V'],
#     '9': ['W','X','Y','Z']
# }
#
# dial = input()
# num = 0
# for i in dial:
#     for key, values in dic_data.items():
#         if i in values:
#             num += int(key)
#     num += 1
#
# print(num)
#
import sys

input = sys.stdin.readline()

numbers = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
alpha = list(input)

result = 0

for i in alpha:
    for j in numbers:
        if i in j:

            result += numbers.index(j) + 3
print(result)



