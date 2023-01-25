# 10828 스택

# import sys
#
# n = int(sys.stdin.readline())
# stack = []
#
# for _ in range(n):
#     order = sys.stdin.readline().split()
#
#     if order[0] in "push":
#         stack.append(order[1])
#     elif order[0] in "top":
#         try:
#             print(stack[-1])
#         except:
#             print(-1)
#     elif order[0] in "size":
#         print(len(stack))
#     elif order[0] in "empty":
#         if len(stack) == 0:
#             print(1)
#         else:
#             print(0)
#     elif order[0] in "pop":
#         try:
#             data = stack.pop(-1)
#             print(data)
#         except:
#             print(-1)
#     else:
#         break


# import sys
#
# n = int(sys.stdin.readline().strip())
#
# for _ in range(n):
#     data = sys.stdin.readline().strip()
#     list_data = data[::-1].split()
#     list_data.reverse()
#     for i in list_data:
#         print(i, end=' ')
#     print()





