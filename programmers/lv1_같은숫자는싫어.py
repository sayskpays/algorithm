
arr = list(map(int, input().split()))
new_arr = list()


# new_arr.append(arr[0])

# for i in arr:
#     if i not in new_arr:
#         new_arr.append(i)
#     else:
#         if new_arr[-1] != i:
#             new_arr.append(i)
#

for i in arr:
# 여기서 new_arr[-1:] 슬라이스는 값이 리스트 이기 때문에 == [i] 이렇게 비교하여 리스트 대 리스트로 값을 비교하기 위해서 이렇게 쓰였다.
    if new_arr[-1:] == [i]: continue

    new_arr.append(i)

print(new_arr)
