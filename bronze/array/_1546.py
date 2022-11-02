import statistics

n = int(input())
num_list = []
avg_num_list = []

i = map(int, input().split()) # 40 80 60
num_list.extend(i) # [40, 80, 60]
max_num = max(num_list) # 80

for i in num_list:
    avg_num_list.append((i / max_num) * 100)

test = statistics.mean(avg_num_list)
print(test)
