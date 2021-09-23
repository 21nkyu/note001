# https://www.acmicpc.net/problem/1978

n = int(input())
o = [None] * 1000
m = list(map(int, input().split()))

for i in m:
    for j in range(2, (i//2)+1):
        if i%j != 0 and i != 1:
            o[i-1] = 1
            
            

print(o.count(1))
    


