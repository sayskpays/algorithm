import bisect

n = int(input())
card = list(map(int,input().split()))
m = int(input())
test = list(map(int,input().split()))
card.sort()

def cnt_by_range(a, left_value, right_value):
    right_index = bisect.bisect_right(a,right_value)
    left_index = bisect.bisect_left(a,left_value)
    return right_index - left_index

for i in range(len(test)):
    print(cnt_by_range(card,test[i],test[i]),end=' ')


