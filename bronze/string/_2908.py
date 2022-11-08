#
# a,b = input().split()
# test = ""
# test_b = ""
# for i in reversed(a):
#     test += i
#
# for i in reversed(b):
#     test_b += i
#
# if int(test) > int(test_b):
#     print(test)
# elif int(test) < int(test_b):
#     print(test_b)

num1 , num2 = input().split()
num1 = int(num1[::-1])
num2 = int(num2[::-1])

if num1 > num2:
    print(num1)
else:
    print(num2)

print(num1) if num1 > num2 else print(num2)

