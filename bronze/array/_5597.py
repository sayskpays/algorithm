
# num_list = []
#
# for _ in range(28):
#     number = int(input())
#     num_list.append(number)
#
# for i in range(1, 31):
#     if i not in num_list:
#         print(i)

# 해설

students = [i for i in range(1,31)]

for _ in range(28):
    number = int(input())
    students.remove(number)

print(min(students))
print(max(students))

