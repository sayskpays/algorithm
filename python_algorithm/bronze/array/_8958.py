n = int(input())

for i in range(n):
    test = input()
    cnt = 0
    hap = 0

    for data in test:
        if data == 'O':
            cnt += 1
            hap += cnt
        elif data == 'X':
            cnt = 0
            
    print(hap)
