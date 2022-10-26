
a = int(input())
b = int(input())
a_list = list(map(int, str(a)))
b_list = list(map(int, str(b)))

first_sum, second_sum, third_sum = 0,0,0

for i in range(len(a_list)):
    first_sum = b_list[2] * a
    second_sum = b_list[1] * a
    third_sum = b_list[0] * a

print(first_sum)
print(second_sum)
print(third_sum)
print(a*b)

# 해설
# A = int(input())  # 첫번째 입력받은 문자 : 숫자로 변환
# B = input()       # 두번째 입력받은 문자 : 문자열 그대로 둠
#
# # 문자열의 인덱스를 이용해서 두번째 입력 받은 문자를 하나씩 숫자로 반환하고 A와 곱한다.
# AxB2 = A * int(B[2])
# AxB1 = A * int(B[1])
# AxB0 = A * int(B[0])
# AxB = A * int(B)
#
# print(AxB2, AxB1, AxB0, AxB, sep='\n')
# # sep='\n'로 줄바꿈








