
s = input()
s_list = list(s)
n = int(input())
answer = ""

for i in s_list:
    asc_data = ord(i)+n
    if i != " ":
        if asc_data <= 90:
            answer += "".join(chr(asc_data))
        elif 91 <= asc_data <= 97:
            answer += "".join(chr(65 + (asc_data - 91)))
        elif asc_data < 123:
            answer += "".join(chr(asc_data))
        else:
            answer += "".join(chr(97+(asc_data-123)))
    else:
        answer += "".join(" ")

print(answer)

