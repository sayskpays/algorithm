arr = list(map(int, input().split()))
divisor = int(input())
new_arr = sorted([x for x in arr if x % divisor == 0]) or [-1] # new_arr이 비어 있으면 -1

print(new_arr)