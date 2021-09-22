# https://www.acmicpc.net/problem/10757

import sys

def sumab(a, b):
    return a+b


a, b = map(int, sys.stdin.readline().split())
print(sumab(a, b))