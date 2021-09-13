# https://www.acmicpc.net/problem/1182

# 자연수 n, m

# 1~n까지 자연수 중에서
# 중복 없이 m개를 고른 수열

from itertools import permutations

n, m = map(int, input().split())

num_list = list(range(1, n+1))

ans = list(permutations(num_list, m))

for i in ans:
    print(*i)