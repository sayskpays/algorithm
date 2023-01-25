# import sys
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
import sys

n = sys.stdin.readline().strip()
m = int(sys.stdin.readline().strip())
stack = list(n)
pointer = len(n) + 1

for _ in range(m):
    ord = sys.stdin.readline().strip()

    if ord == "L":
        if pointer == 0:
            pass
        else:
            pointer -= 1
    elif ord == "D":
        if pointer > len(n) + 1:
            pass
        else:
            pointer += 1
    elif ord == "B":
        if pointer <= 0:
            pass
        else:
            stack.pop(pointer-1)
    else:
        stack.insert(pointer, ord.split(" ")[1])

print("".join(stack))
