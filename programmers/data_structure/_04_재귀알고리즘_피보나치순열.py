
def solution(x):

    if x == 0:
        return 0
    elif x == 1:
        return 1
    else:
        return solution(x-1) + solution(x-2)

n = int(input("Number : "))
print(solution(n))

def solution(x):
    s = 0
    while x >= 2:
        s += (x-1) + (x-2)
        x -= 1
    return s

n = int(input("Number : "))
print(solution(n))


