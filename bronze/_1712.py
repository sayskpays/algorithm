import sys

input = sys.stdin.readline()
FIXED_COST, VARIABLE_COST, PRICE = map(int, input.split())

if VARIABLE_COST >= PRICE:
    print(-1)
else:
    print(int(FIXED_COST/(PRICE-VARIABLE_COST))+1)
