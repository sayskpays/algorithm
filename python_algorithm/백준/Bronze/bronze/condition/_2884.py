time, minute = map(int, input().split())

minus_minute = 45

if 0 <= time <= 23 and 0 <= minute <= 59:

    if minute < minus_minute:
        if time == 0:
            time = 24 - 1
        else:
            time = time - 1

        minute = (minute+60) - minus_minute
    elif minute >= minus_minute:
        minute = minute - minus_minute
    else:
        minute = 0

print(time, minute)

# 해설

# H, M = map(int, input().split())
#
# if M < 45:  # 분단위가 45분보다 작을 때
#     if H == 0:  # 0 시이면
#         H = 23
#         M += 60
#     else:  # 0시가 아니면 (0시보다 크면)
#         H -= 1
#         M += 60
#
# print(H, M - 45)



