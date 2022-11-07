
# test = set()
# set_data = set(range(1,10001))
#
# for i in range(1, 10001):
#     if len(str(i)) <= 2:
#         data = i + (i % 10) + (i // 10)
#         test.add(data)
#     elif len(str(i)) == 3:
#         data = i + (i % 10) + (i // 10)
#
# self_num = sorted(set_data - test)
#
# for data in sorted(self_num):
#     print(data, sep="\n")

natural_num = set(range(1,10001))
generated_num = set()

for i in range(1, 10001):
    for j in str(i):
        i += int(j)
    generated_num.add(i)

self_num = sorted(natural_num - generated_num)

for i in self_num:
    print(i)


