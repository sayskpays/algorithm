
numbers = list(map(int, input().split()))
k = int(input())
idx = numbers[(k-1)*2 % len(numbers)]

print(idx)