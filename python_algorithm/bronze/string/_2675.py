#
# test_case = int(input())
# new_list = []
# new_data =""
# for _ in range(test_case):
#     a,b = map(str, input().split())
#
#     for i in range(len(b)):
#         new_list.extend(int(a) * b[i])
#     new_data = ''.join(new_list)
#     print(new_data)
#     new_list.clear()

t = int(input())
for _ in range(t):
    num, s = input().split()
    text = ''
    for i in s:
        text += int(num) * i
    print(text)