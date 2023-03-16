# n = input()
# arr = []
# start = n[0]
# for i in n:
#     if start == i:
#         continue
#     else:
#         start = i
#         arr.append(1)
#
# print((arr.count(1)+1) // 2)

s = input()

cnt = 0
for i in range(len(s) -1):
    if s[i] != s[i+1]:
        cnt += 1
print((cnt+1) // 2)