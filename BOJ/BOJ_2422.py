# https://www.acmicpc.net/problem/2422

n, m = map(int, input().split())

t_c = sum(list(range((n-m)+2)))

print(t_c-m)


from itertools import combinations




