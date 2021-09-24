# https://www.acmicpc.net/problem/5534

n = int(input())
m = input()
mm = [input() for _ in range(n)]
mmm =[]
print(mm)
cnt = 0
for i in mm:
    for j in i:
        if j in m:
            i.replace(j, '')
        

print(cnt)

