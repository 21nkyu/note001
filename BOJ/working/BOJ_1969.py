# https://www.acmicpc.net/problem/1969

# a = set('TATGATAC')
# b = set('TAAGCTAC')

# print(len(a|b))



n, m = map(int, input().split())
ncltd = [input() for _ in range(n)]
print(ncltd)
# cnt = 0
for i in ncltd:
    for j in ncltd:
        print(i, j)        
        if i == j:
            continue
        elif i != j:
            diff = list(set(i)|set(j))
            print(diff)
            # cnt+=diff

# print(cnt)

