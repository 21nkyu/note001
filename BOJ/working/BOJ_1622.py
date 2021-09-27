# https://www.acmicpc.net/problem/1622

def rc(a, b):
    c = list(set(a) & set(b))
    c = sorted(c)
    print(''.join(c))
    return rc(a = input(), b=input())

a=input()
b=input()
rc(a, b)