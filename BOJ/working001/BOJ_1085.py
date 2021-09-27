# https://www.acmicpc.net/problem/1085

x,y,w,h = map(int, input().split())

if w>x and h>y:
    print(min(w-x, h-y))
elif w>x and h<y:
    print(min(w-x, y-h))
elif w<x and h>y:
    print(min(x-w, h-y))
elif w<x and h<y:
    print(min(x-y, y-h))