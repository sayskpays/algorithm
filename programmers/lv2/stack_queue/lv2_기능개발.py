def solution(progresses, speeds):

    data = []
    stack = []
    i = 0

    for j in range(len(progresses)):
        susic = (100-progresses[j]) // speeds[j]
        data.append(susic + 1 if susic * progresses[j] < 100 else susic)

    while i < len(progresses):

        if not stack:
            stack.append(data[i])
            i += 1

        if data[i] < stack[i-1]:
            data.pop(i)
            stack.append(stack[i-1])
        else:
            stack.append(data[i])
            i += 1

print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))