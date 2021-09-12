# https://www.acmicpc.net/problem/2775

def floor(n):
    if n == 1:
        return 1
    return n + floor(n-1)

n=int(input())
print(floor(n))