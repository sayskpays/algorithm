
# 입력한 숫자를 1씩 감소시켜 합을 구하기 (재귀함수 사용)

def sum(n):

    if n <= 1:
        return n
    else:
        return n + sum(n-1)

a = int(input("Number : "))
print(sum(a))

# 일반적인 반복문(Iterative) 과의 효율은 ?

def sum1(n):
    s = 0
    while n >= 0:
        s += n
        n -= 1
    return s

# n! 을 구하는 재귀 알고리즘 예제

def what(n):
    if n<=1:
        return 1
    else:
        return n * what(n - 1)
