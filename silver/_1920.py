# # 수 찾기 (Silver 4)
#
# n = int(input())
# a = list(map(int, input().split()))
# a.sort()
#
# m = int(input())
# b = list(map(int, input().split()))
#
# answer = []
# i = 0
# for _ in range(len(b)):
#     lower = 0
#     upper = len(b) - 1
#     middle = (lower + upper) // 2
#
#     if b[i] not in a:
#         answer.append(0)
#         i += 1
#     else:
#         while lower <= upper:
#             middle = (lower + upper) // 2
#
#             if a[middle] == b[i]:
#                 answer.append(1)
#                 i += 1
#                 break
#             elif a[middle] < b[i]:
#                 lower = middle + 1
#             else:
#                 upper = middle - 1
#
# print(*answer,sep='\n')

N = int(input())
A = list(map(int, input().split()))
M = int(input())
arr = list(map(int, input().split()))
A.sort()

# arr의 각 원소별로 이분 탐색
for num in arr:
    lt, rt = 0, N -1
    isExist = False

    # 이분 탐색 시작
    while lt <= rt:
        mid = (lt+rt) // 2
        if num == A[mid]:
            isExist = True
            print(1)
            break
        elif num > A[mid]:
            lt = mid + 1
        else:
            rt = mid - 1

    if not isExist:
        print(0)


