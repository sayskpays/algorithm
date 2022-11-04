x = 1
test = set()
set_data = set(list(range(1,10001)))

while 1:
    data = x + (x % 10) + (x // 10)
    test.add(data)
    new_data = set_data - test
    x += 1
    if max(test) >= 10000:
        break

for data in sorted(new_data):
    print(data, sep="\n")
