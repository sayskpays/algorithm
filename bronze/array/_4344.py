import statistics

test_case_n = int(input())

for _ in range(test_case_n):
    cnt = 0
    score_list = list(map(int, input().split()))
    stu_num= score_list.pop(0)

    avg = statistics.mean(score_list)

    for data in score_list:
        if data > avg:
            cnt += 1

    hong = round((cnt*100)/stu_num,3)
    print(f"{hong:.3f}%")
