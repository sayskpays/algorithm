
list_data = list()
while True:
    input_data = int(input())
    for i in range(input_data, 2*input_data):
        if i == 1:
            continue
        for j in range(2, int(i**0.5)+1):
            if i%j == 0:
                break
        else:
            list_data.append(i)
    print(len(list_data))

    # 	시간 초과