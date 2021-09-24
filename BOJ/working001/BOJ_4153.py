# https://www.acmicpc.net/problem/4153

while True:
    n=list(map(int, input().split()))
    n=sorted(n)
    if sum(n) == 0:
        break
    elif n[0]**2 + n[1]**2 == n[2]**2:
        print('right')
    else:
        print('wrong')