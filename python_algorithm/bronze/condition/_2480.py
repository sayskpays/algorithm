#
# A,B,C = map(int,input().split())
# price = 0
#
# all_same = A == B and B == C and A == C
# two_same = A == B or B == C or A == C
# not_same = A != B and B != C and A != C
#
# if all_same:
#     price = 10000 + (A) * 1000
# elif two_same:
#     if A == B:
#         price = 1000 + (A) * 100
#     elif B == C:
#         price = 1000 + (B) * 100
#     elif A == C:
#         price = 1000 + (C) * 100
# elif not_same:
#     price = max(A,B,C) * 100
#
# print(price)

# 해설

A,B,C = map(int,input().split())

if A==B==C:
    print(10000+A*1000)
elif A==B:
    print(1000+A*100)
elif A==C:
    print(1000+A*100)
elif B==C:
    print(1000+B*100)
else:
    print(100*max(A,B,C))
