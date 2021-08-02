import sys
T = int(sys.stdin.readline())

for _ in range(T):
    a, b = map(int, sys.stdin.readline().split())
    i = a**b
    j = (i//10)*10
    print(i-j)


        