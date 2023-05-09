import time

start_time = time.time()

def solution(progresses, speeds):

    answer = []
    time = 0
    count = 0

    while len(progresses) > 0:
        if progresses[0] + time * speeds[0] >= 100:
            progresses.pop(0)
            speeds.pop(0)
            count += 1
        else:
            if count > 0:
                answer.append(count)
                count = 0
            time += 1
    answer.append(count)
    return answer

end_time = time.time()
print(end_time-start_time)

print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))
