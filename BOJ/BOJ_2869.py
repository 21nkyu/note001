# https://www.acmicpc.net/problem/2869

a, b, v = map(int, input().split())

# day = v//(a+b)

if (a-b)//2 == 0:
    day = v//(a-b) - 1
    print(day)
else:
    day = v//(a-b) + 1
    print(day)