
s = input()
new_arr = []
answer = []


for i in range(len(s)):
    if s[i] not in new_arr:
        answer.append(-1)
    elif s[i] in new_arr:
        if new_arr.count(s[i]) >= 2:
            new_arr.pop(new_arr.index(s[i]))
            idx_cnt = i - (new_arr.index(s[i])+1)
        else:
            idx_cnt = i - new_arr.index(s[i])
        answer.append(idx_cnt)
    new_arr.append(s[i])

# for i in s:
#     if i not in new_arr:
#         new_arr.append(i)
#         answer.append(-1)
#     elif i in new_arr:
#         idx_cnt = s.index(i) - new_arr.index(i)
#         answer.append(idx_cnt)

# 아직 해설 보지 않음 !!!!!!!!!!!

print(answer)