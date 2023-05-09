
s = input()
s_list = list(s)
n = int(input())

for i in s_list:
    asc_data = ord(i)+n
    if i != " ":
        if asc_data <= 90:
            print(chr(asc_data),end='')
        elif 91 <= asc_data <= 97:
            print(chr(65 + (asc_data - 91)),end='')
        elif asc_data < 123:
            print(chr(asc_data),end='')
        else:
            print(chr(97+(asc_data-123)),end='')
    else:
        print(" ",end='')



