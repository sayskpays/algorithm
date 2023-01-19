from itertools import combinations


# def is_prime_number(num):
#     if num == 0 or num == 1:
#         return False
#     else:
#         for i in range(2, (num // 2) + 1):
#             if num % i == 0:
#                 return False
#
#         return True
#
#
# def solution(nums):
#     answer = 0
#     cmb = list(combinations(nums, 3))
#     for arr in cmb:
#         if is_prime_number(sum(arr)):
#             answer += 1
#     return answer
#
#
# print(solution([1, 2, 7, 6, 4]))

def is_last_check(num, budget):
    if num % budget == 0:
        return False
    else:
        return True


def solution(d, budget):
    answer = 1

    while True:
        cmb = list(combinations(d, answer))
        for i in cmb:
            if is_last_check(sum(i), budget):
                continue
            else:
                answer += 1
    return answer


print(solution([1, 3, 5, 2, 4], 9))
