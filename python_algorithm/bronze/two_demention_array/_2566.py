import random

random_list_a = [[random.randint(1, 99) for j in range(9)] for i in range(9)]
max_list = []

for i in range(9):
    for j in range(9):
        print(random_list_a[i][j],end=" ")
    max_list.append(max(random_list_a[i]))
    print()

print(max(max_list))
