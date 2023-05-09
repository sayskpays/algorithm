
m = int(input())
n = int(input())
data_list = list()
num = 0

for data in range(m, n+1):
    for i in range(2, n+1):
        if data % i == 0:
            if data == i:
                data_list.append(data)
                num += data
            break

if not data_list:
    print("-1")
else:
    print(num)
    print(min(data_list))



