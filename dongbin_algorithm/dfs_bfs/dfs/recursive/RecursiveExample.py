
# 2가지로 구현한 팩토리얼 예제 ( 재귀 함수 )


# 반복문으로 구현 iterative
def factorial_iterative(n):
    result = 1
    # 1부터 n까지의 수를 차례대로 곱하기
    for i in range(1, n+1):
        result *= i
    return result

# 재귀적으로 구현 recursive
def factorial_recursive(n):
    if n <= 1: # n이 1 이하인 경우 1을 반환
        return 1
    # n != n * (n - 1) n! 구하는 코드를 그대로 작성
    return n * factorial_recursive(n -1)

print('반복적으로 구현:', factorial_iterative(5))
print('재귀적으로 구현:', factorial_recursive(5))

