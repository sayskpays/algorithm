import bisect

L = sorted(list(map(int, input().split())))
x = int(input())


def answer(a, left_value, right_value):
    left_index = bisect.bisect_left(a, left_value)
    return left_index


if x in L:
    print(answer(L, x, x))
else:
    print(-1)
