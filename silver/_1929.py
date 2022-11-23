import sys

input = sys.stdin.readline()
m,n = map(int,input.split())

data_list = [x for x in range(m, n+1) if x%2 != 0 and x%3 != 0]

if m == 2:
    data_list.insert(0,2)
elif m == 3:
    data_list.insert(0,3)
for data in data_list:
    print(data)



