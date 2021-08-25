# https://www.acmicpc.net/problem/11047n, k  = map(int, input().split())
n, k  = map(int, input().split())
coin_vals = []

for _ in range(n):
    c = int(input())
    coin_vals.append(c)
coin_vals = coin_vals[::-1]    

coin_cnt = 0
for coin_val in coin_vals:
    coin_cnt += k//coin_val
    k %= coin_val

print(coin_cnt)