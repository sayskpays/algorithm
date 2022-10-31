# 해설

n = int(input())
num = n
cnt = 0

while True:
    a = num // 10 # 2
    b = num % 10 # 6
    c = (a+b) % 10 # 1"4"
    num = (b*10) + c

    cnt = cnt + 1
    if(num==n):
        break

print(cnt)

# n = input()
# num = n
# cnt = 0
#
# while 1:
#     if len(num) == 1:
#         num = "0"+num
#     plus = str(int(num[0]) + int(num[1]))
#     num = num[-1] + plus[-1]
#     cnt += 1
#
#     if num == n:
#         print(cnt)
#         break


#
# N = input() # 55
# count = 0
# plus = 0
# new_plus = 0
#
# while True:
#     try:
#         if len(N) == 2:
#             plus = int(N[0])+int(N[1]) # 8
#             if len(str(plus))==1:
#                 N = str(plus)
#             elif len(str(plus))==2:
#                 N = str(plus[1])
#             count += 1
#             continue
#
#         elif len(N) == 1:
#             plus = str(N[0]+"0")
#             int(plus)
#             count += 1
#
#         if plus == int(N):
#             print(count)
#             break
#     except:
#         break
#
#



