# https://www.acmicpc.net/problem/18868

from itertools import combinations

# a = [1,3,2]
# combi = combinations(a,2)

# print(list(combi))

m = int(input())
mmm = []
for _ in range(m):
    mm = list(map(int, input().split()))
    mmm.append(mm)
    mmmm = combinations(mmm,2)
print(mmm)
print(list(mmmm))



