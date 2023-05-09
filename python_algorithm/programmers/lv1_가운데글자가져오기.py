s = input()

if len(s) % 2 == 0:
    mid = (len(s) -1) // 2
    print(s[mid:mid+2])
else:
    mid = len(s) // 2
    print(s[mid])

# 다른 사람 풀이법 : return s[(len(str)-1)//2:len(s)//2+1]
