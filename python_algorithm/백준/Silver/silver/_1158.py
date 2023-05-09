import sys

n, k = list(map(int,sys.stdin.readline().split()))
arr = [x for x in range(1, n+1)]
queue = []
num = 0

for _ in range(n):
    num += k-1
    if num >= len(arr):
        num = num % len(arr)

    queue.append(arr.pop(num))

print("".join(str(queue)).replace("[", "<").replace("]", ">"))