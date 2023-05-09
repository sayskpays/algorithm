# 9012 번 실버 4 괄호
import sys

t = int(sys.stdin.readline().strip())

# 해설

for _ in range(t):
    stack = []
    a = sys.stdin.readline().strip()
    for i in a:
        if i == "(":
            stack.append(i)
        elif i == ")":
            if stack:
                stack.pop()
            else:
                print("NO")
                break
    else: # break 문으로 끊이지 않고 for문이 실행 되었을 때
        if not stack:
            print("YES")
        else:
            print("NO")

# 내가 푼 코드

# for _ in range(t):
#     low_data = sys.stdin.readline().strip()
#     low_data = low_data.replace("()", "")
#
#     if low_data.count("(") == low_data.count(")") and low_data.endswith(")"):
#         print("YES")
#     else:
#         print("NO")