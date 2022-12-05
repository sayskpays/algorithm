
n=list(map(int,input().split()))
cnt=len(n)//2
n=set(n)

if len(n) > cnt:
    print(cnt)
else:
    print(len(n))