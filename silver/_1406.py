# 내가 푼 코드 (시간 초과)

# import sys
#
# n = sys.stdin.readline().strip()
# m = int(sys.stdin.readline().strip())
# stack = list(n)
# pointer = len(n) + 1
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
#             stack.pop(pointer-1)
#     else:
#         stack.insert(pointer, ord.split(" ")[1])
#
# print("".join(stack))
