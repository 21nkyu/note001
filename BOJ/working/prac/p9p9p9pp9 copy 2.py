# n%k != n-1
# n//k == 0 n//k

n, k = map(int, input().split())

total_cnt = 0

while True:
    if n//k != 0:
        n = n-1
        total_cnt += 1
    elif n//k == 0:
        n = n//k
        total_cnt += 1
    elif n//k == 1:
        print(total_cnt)
        break

print(total_cnt)