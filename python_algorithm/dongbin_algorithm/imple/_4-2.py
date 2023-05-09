
h = int(input())

count = 0
for i in range(h+1):
    for j in range(60):
        for k in range(60):
            # 매 시각 안에 '3'이 포함되어 있다면 카운트 증가
            if '3' in str(i) + str(j) + str(k):
                count += 1

print(count)

# 예를 들어 03시 20분 35초일 때를 확인한다면,
# '032035'로 만ㄷ르어서 3이 포함되어 있는지 체크
