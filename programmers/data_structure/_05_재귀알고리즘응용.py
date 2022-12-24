
# n 개의 서로 다른 원소에서 m 개를 택하는 경우의 수

from math import factorial as f

def combi(n,m):
    return f(n) / (f(m) * f(n-m))