
N = input() # 55
count = 0
plus = 0
new_plus = 0

while True:
    try:
        if len(N) == 2:
            plus = int(N[0])+int(N[1]) # 8
            if len(str(plus))==1:
                N = str(plus)
            elif len(str(plus))==2:
                N = str(plus[1])
            count += 1
            continue

        elif len(N) == 1:
            plus = str(N[0]+"0")
            int(plus)
            count += 1

        if plus == int(N):
            print(count)
            break
    except:
        break



