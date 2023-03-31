
n = input()

temp = n.replace('XXXX', 'AAAA')
temp = temp.replace('XX', 'BB')

if 'X' in temp:
    print(-1)
else:
    print(temp)