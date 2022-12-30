
a = int(input())
b = int(input())
num = 0

# if a <= b:
#     for i in range(a,b+1):
#         num += i
# else:
#     for i in range(b, a+1):
#         num += i

if a > b :
    a, b = b, a
num = sum(range(a, b+1))


print(num)
