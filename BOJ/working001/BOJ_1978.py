# https://www.acmicpc.net/problem/1978

n = int(input())
o = [None] * 1000
m = list(map(int, input().split()))

for i in m:
    if i ==1:
            o[i-1] = None
    for j in range(2, i):        
        if i%j != 0:
            o[i-1] = 1

print(o.count(1))           
            
print(o[0:10])

    


