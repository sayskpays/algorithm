import sys

word = list(sys.stdin.readline().rstrip())

i = 0
start = 0

while i < len(word):
    if word[i] == "<":
        i += 1
        while word[i] != ">":
            i += 1
        i += 1

    elif word[i].isalnum():
        start = i
        while i < len(word) and word[i].isalnum():
            i += 1
        tmp = word[start:i]
        tmp.reverse()
        word[start:i] = tmp
    else:
        i += 1 # 괄호도 아니고 알파벳, 숫자도 아닌 것은 공백이므로
                # 그냥 인덱스 증가 시킨다.

print("".join(word))