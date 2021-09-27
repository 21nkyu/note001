# https://www.acmicpc.net/problem/17266

# n 길이
# m 개수
# 설치위치 l1, l2
# 최악의 경우만 계산하면 됨


# import sys

# sys.setrecursionlimit(10**6)


# def sl(l, s, f):
#     return max(l[0]-s, f-l[0])

# def nsl(l, s, f, h_m, i):
#     if i == len(l):
#         return h_m

#     for i in range(len(l)):
#         if i == 0:
#             h = l[i] - s
#         elif i == len(l)-1:
#             h = f - l[i]
#         else:
#             if (l[i]-l[i-1])%2:
#                 h = ((l[i]-l[i-1])//2) + 1
#             else:
#                 h = (l[i]-l[i-1])//2

#     return max(h_m, nsl(l, s, f, max(nsl(l, s, f, h), h_m), i))

# n = int(input())
# m = int(input())
# l = list(map(int, input().split()))
# s, f = 0, n
# i = 0
# h_m=0


# if len(l)==1:
#     print(sl(l,s,f))
# else:
#     print(nsl(l,s,f,h_m,i))

#============================================

n = int(input())
m = int(input())
l = list(map(int, input().split()))
s, f = 0, n
h_m=0

if len(l) == 1:
    h_m = max(l[0]-s, f-l[0])
else:
    for i in range(len(l)):
        if i == 0:
            h = l[i] - s
        elif i == len(l)-1:
            h = f - l[i]
        else:
            if (l[i]-l[i-1])%2:
                h = ((l[i]-l[i-1])//2) + 1
            else:
                h = (l[i]-l[i-1])//2
        h_m = max(h, h_m)

print(h_m)


#========================================================

n = int(input())
m = int(input())
l = list(map(int, input().split()))
s, f = 0, n

if len(l) == 1:
    print(max(l[0]-s, f-l[0]))
else:
    if len(l) > 1 and (l[1] - l[0])%2 != 0:
        print(max(((l[1] - l[0])//2)+1, l[0]-s, f-l[-1]))
    elif len(l) > 1 and (l[1] - l[0])%2 == 0:
        print(max(((l[1] - l[0])//2), l[0]-s, f-l[-1]))
