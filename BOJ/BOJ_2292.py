T = int(input())

for _ in range(T):
    a, b = map(int, input().split())
    i = a**b
    print(str(i)[-1])