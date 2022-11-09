# import sys

# input = sys.stdin.readline().strip()
# CROATIAN_ALPHABET = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
# input_data = input
# result = 0
#
# for i in CROATIAN_ALPHABET:
#     if 'dz=' in input_data and 'z=' in input_data:
#         result += 3
#         if i in input_data:
#             result += 2
#     else:
#         continue
# print(result)
CROATIAN_ALPHABET = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
word = input()

for i in CROATIAN_ALPHABET:
    word = word.replace(i, '*')
print(len(word))


