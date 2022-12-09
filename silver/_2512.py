n = int(input())
tax = list(map(int, input().split()))
m = int(input())
lower = 0
upper = len(tax) -1
num = 0
tax_sum = sum(tax)
tax.sort()

if tax_sum <= m:
    print(max(tax))
else:
    while lower <= upper:
        middle = (lower + upper) // 2

        if (m//n) >= tax[middle]:
            num = sum(tax[:middle+1])
            del tax[:middle+1]
            lower = middle -1
            break
        else:
            upper = middle -1

    print((m-num)//len(tax))