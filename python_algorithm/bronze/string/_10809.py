
s = input().lower()

alpha = [i for i in range(ord('a'), ord('z')+1)]
output_data = []

for i in alpha:
    try:
        output_data.append(s.index(chr(i)))
    except:
        output_data.append(-1)

print(*output_data, end=" ")
