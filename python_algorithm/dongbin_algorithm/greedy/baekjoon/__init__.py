
# n = input()
#
# if n.count('X') % 2 != 0:
#     print(-1)
#     exit(0)
#
# temp = n.replace('XXXX', 'AAAA')
# temp = temp.replace('XX', 'BB')
#
# print(temp)

#
# n = input()
#
# temp = n.replace('XXXX', 'AAAA')
# temp = temp.replace('XX', 'BB')
#
# if 'X' in temp:
#     print(-1)
# else:
#     print(temp)

from collections import deque

a = [1,2,3]
q = deque(a)
print(len(q))
