import sys
#
# n = int(sys.stdin.readline().strip())
# stack = []
# answer = []
# flag = 0
# cur = 1
#
# for i in range(n):
#     num = int(sys.stdin.readline().strip())
#     while cur <= num:
#         stack.append(cur)
#         answer.append("+")
#         cur += 1
#
#     if stack[-1] == num:
#         stack.pop()
#         answer.append("-")
#     else:
#         print("NO")
#         flag = 1
#         break
#
# if flag == 0:
#     for i in answer:
#         print(i)


# n = sys.stdin.readline().strip()
# m = int(sys.stdin.readline().strip())
# stack = list(n)
# pointer = len(n)
#
# for _ in range(m):
#     ord = sys.stdin.readline().strip()
#
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
#             if pointer >= len(n):
#                 stack.pop()
#             else:
#                 stack.pop(pointer-1)
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

