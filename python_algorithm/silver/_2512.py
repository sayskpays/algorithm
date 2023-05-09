# 내가 푼 풀이

# n = int(input())
# tax = list(map(int, input().split()))
# m = int(input())
# lower = 0
# upper = len(tax) -1
# num = 0
# tax_sum = sum(tax)
# tax.sort()
#
# if tax_sum <= m:
#     print(max(tax))
# else:
#     while lower <= upper:
#         middle = (lower + upper) // 2
#
#         if (m//n) >= tax[middle]:
#             num = sum(tax[:middle+1])
#             del tax[:middle+1]
#             lower = middle -1
#             break
#         else:
#             upper = middle -1
#
#     print((m-num)//len(tax))

import sys
input = sys.stdin.readline()

N = int(input())
budge_list = list(map(int, input().split()))
budget = int(input())
start, end = 0, max(budge_list)

# 이분 탐색
while start <= end:
    mid = (start + end) // 2
    total = 0 # 총 지출 양
    for i in budge_list:
        if i > mid:
            total += mid
        else:
            total += i
    if total <= budget: # 지출 양이 예산 보다 작으면
        start = mid + 1
    else: # 지출 양이 예산 보다 크면
        end = mid -1
print(end)







