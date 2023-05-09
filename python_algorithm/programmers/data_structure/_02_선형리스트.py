
list_data = list(map(int,input().split()))

x = int(input())

for i in range(len(list_data)):
    if list_data[i] >= x:
        list_data.insert(i,x)
        break
    elif list_data[-1] < x:
        list_data.append(x)

print(list_data)
