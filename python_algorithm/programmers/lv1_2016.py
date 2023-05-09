
# import calendar
#
# def solution(a, b):
#     week = ["MON","TUE","WED","THU","FRI","SAT","SUN"]
#
#     answer = week[calendar.weekday(2016,a,b)]
#     return answer
# print(calendar.weekday(2016,5,22))

months = [31,29,31,30,31,30,31,31,30,31,30,31]
days = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']

print(days[(sum(months[:5-1])+24-1)%7])