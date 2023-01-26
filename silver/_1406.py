# 내가 푼 코드 (시간 초과)

import sys
#
# n = sys.stdin.readline().strip()
# m = int(sys.stdin.readline().strip())
# stack = list(n)
# pointer = len(n) + 1
#
# for _ in range(m):
#     ord = sys.stdin.readline().strip()

#     if ord == "L":
#         if pointer == 0:
#             pass
#         else:
#             pointer -= 1
#     elif ord == "D":
#         if pointer > len(n) + 1:
#             pass
#         else:
#             pointer += 1
#     elif ord == "B":
#         if pointer <= 0:
#             pass
#         else:
#             stack.pop(pointer-1)
#     else:
#         stack.insert(pointer, ord.split(" ")[1])
#
# print("".join(stack))

# 해설

st1 = list(sys.stdin.readline().rstrip())
st2 = []

for _ in range(int(sys.stdin.readline())):
    command = list(sys.stdin.readline().split())

    if command[0] == 'L':
        if st1:
            st2.append(st1.pop())

    elif command[0] == 'D':
        if st2:
            st1.append(st2.pop())

    elif command[0] == 'B':
        if st1:
            st1.pop()

    else:
        st1.append(command[1])

st1.extend(reversed(st2))
print(''.join(st1))
