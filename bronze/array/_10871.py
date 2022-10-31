
n,x= map(int,input().split())

data_list = list(map(int,input().split()))

if n == len(data_list):
    for i in data_list:
        if i < x:

            print(data_list[i], end=" ")



