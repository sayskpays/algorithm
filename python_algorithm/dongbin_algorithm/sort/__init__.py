
# 선택 정렬

# arr = [7,5,9,0,3,1,6,2,4,8]
#
# for i in range(len(arr)):
#     min_index = i # 가장 작은 원소의 인덱스
#     for j in range(i+1, len(arr)):
#         if arr[min_index] > arr[j]:
#             min_index = j
#     arr[i], arr[min_index] = arr[min_index], arr[i]
#
# print(arr)

# 삽입 정렬

array = [7,5,9,0,3,1,6,2,4,8]

for i in range(1, len(array)):

    for j in range(i, 0, -1): # 인덱스 i 부터 1까지 감소하며 반복
        if array[j] < array[j - 1 ]: # 한 칸씩 왼쪽으로 이동
            array[j], array[j-1] = array[j-1], array[j]
        else: # 자기보다 작은 데이터를 만나면 그 위치에서 멈춤
            break

print(array)

# range의 매개 변수는 3개(start, end, step)이다.
# 세 번째 매개 변수인 step에 -1이 들어가면 start 인덱스부터
# 시작해서 end + 1 인덱스까지 1씩 감소한다.
# 앞의 코드에서는 j 변수가 i 부터 1까지 1씩 감소한다.
