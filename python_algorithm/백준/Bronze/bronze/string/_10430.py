# 푼 문제

# (a, b, c) = list(map(int, input().split()))
#
# print((a+b) % c)
# print((a % c) + (b % c) % c)
# print((a * b) % c)
# print((a % c) * (b % c) % c)

# 답안

A,B,C = map(int,input().split())
print((A+B)%C, ((A%C)+(B%C))%C, (A*B)%C, ((A%C)*(B%C))%C, sep='\n')


