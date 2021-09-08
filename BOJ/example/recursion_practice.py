#최대공약수 유클리드 호제법
# GCD(192, 162)
# GCD(192, 162)->GCD(162,30->GCD(30,12))->GDC(12,6)->GDC(2)
import sys
import math
sys.setrecursionlimit(10**6)

def gcd(a, b):
    if a%b == 0:
        return b
    return gcd(b, a%b)

c, b = map(int, input().split())
a = math.factorial(c)
print(gcd(a, b))

#==========================================

import sys
sys.setrecursionlimit(10**6)

def gcd(a, b):
    if a%b == 0:
        return b
    return gcd(b, a%b)

def base(c):
    if c == 1:
        return 1
    return c * base(c-1)

c, b = map(int, input().split())
a = base(c)
print(gcd(a, b))



#===================================

def gcd(a, b):
    if a%b == 0:
        return b
    return gcd(b, a%b)

def base(c):
    if c == 1:
        return 1
    return c * base(c-1)

# print(base(3))
# print(base(10))
# print(gcd(72,30))
# print(gdc(10, 240))
# print(gcd(6, 10))
# print(base(3))
# print(gcd(base(3), 240))

c, b = map(int, input().split())
a = base(c)
print(gcd(a, b))