def solution(s):
    s = list(s)
    stack = []

    if s[0] == ')' or s[-1] == '(':
        return False

    for i in range(len(s)):
        if s[i] == '(':
            stack.append('(')
        else:
            if stack:
                stack.pop()

    return len(stack) == 0

print(solution("()()"))