# https://www.acmicpc.net/problem/10872
# import sys
# sys.setrecursionlimit(10**6)

# def fac(n):
#     if n <= 1:
#         return 1
#     return n * fac(n-1)

# n = int(input())
# print(fac(n))

#============================recursion error / 메모리 초과

n = int(input())

ms = 1
for i in range(1, n+1):
    cal1 = i
    ms = ms * cal1
print(ms)

#============================합격